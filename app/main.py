"""
FastAPI application entry point with PostgreSQL
"""
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import List
import uuid

from app.database import engine, get_db, Base
from app.models import Patient, Appointment

# Create tables
Base.metadata.create_all(bind=engine)

# Create FastAPI instance
app = FastAPI(
    title="Healthcare Appointment API",
    description="API for managing patient appointments with PostgreSQL",
    version="0.2.0"
)

# Pydantic models for request/response
class PatientCreate(BaseModel):
    name: str = Field(..., min_length=1)
    age: int = Field(..., ge=0, le=150)
    condition: str = Field(..., min_length=1)

class PatientResponse(BaseModel):
    id: str
    name: str
    age: int
    condition: str
    registered_at: str

class AppointmentCreate(BaseModel):
    patient_id: str
    doctor_id: str
    days_from_now: int = Field(..., ge=1, le=365)

class AppointmentResponse(BaseModel):
    id: str
    patient_id: str
    doctor_id: str
    scheduled_for: str

@app.get("/")
def root():
    return {
        "service": "Healthcare Appointment API",
        "version": "0.2.0",
        "status": "running",
        "database": "PostgreSQL"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "database": "connected"}

@app.post("/patients", response_model=PatientResponse, status_code=201)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    """Create a new patient"""
    db_patient = Patient(
        name=patient.name,
        age=patient.age,
        condition=patient.condition
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    
    return PatientResponse(
        id=str(db_patient.id),
        name=db_patient.name,
        age=db_patient.age,
        condition=db_patient.condition,
        registered_at=db_patient.registered_at.isoformat()
    )

@app.get("/patients", response_model=List[PatientResponse])
def list_patients(db: Session = Depends(get_db)):
    """Get all patients"""
    patients = db.query(Patient).all()
    return [
        PatientResponse(
            id=str(p.id),
            name=p.name,
            age=p.age,
            condition=p.condition,
            registered_at=p.registered_at.isoformat()
        )
        for p in patients
    ]

@app.get("/patients/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: str, db: Session = Depends(get_db)):
    """Get patient by ID"""
    try:
        patient_uuid = uuid.UUID(patient_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid patient ID format")
    
    patient = db.query(Patient).filter(Patient.id == patient_uuid).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    return PatientResponse(
        id=str(patient.id),
        name=patient.name,
        age=patient.age,
        condition=patient.condition,
        registered_at=patient.registered_at.isoformat()
    )

@app.post("/appointments", response_model=AppointmentResponse, status_code=201)
def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    """Schedule an appointment"""
    # Verify patient exists
    try:
        patient_uuid = uuid.UUID(appointment.patient_id)
        doctor_uuid = uuid.UUID(appointment.doctor_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")
    
    patient = db.query(Patient).filter(Patient.id == patient_uuid).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    # Create appointment
    scheduled_time = datetime.utcnow() + timedelta(days=appointment.days_from_now)
    
    db_appointment = Appointment(
        patient_id=patient_uuid,
        doctor_id=doctor_uuid,
        scheduled_for=scheduled_time
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    
    return AppointmentResponse(
        id=str(db_appointment.id),
        patient_id=str(db_appointment.patient_id),
        doctor_id=str(db_appointment.doctor_id),
        scheduled_for=db_appointment.scheduled_for.isoformat()
    )

@app.get("/doctors/{doctor_id}/schedule", response_model=List[AppointmentResponse])
def get_doctor_schedule(doctor_id: str, db: Session = Depends(get_db)):
    """Get all appointments for a doctor"""
    try:
        doctor_uuid = uuid.UUID(doctor_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid doctor ID format")
    
    appointments = db.query(Appointment).filter(
        Appointment.doctor_id == doctor_uuid
    ).all()
    
    return [
        AppointmentResponse(
            id=str(a.id),
            patient_id=str(a.patient_id),
            doctor_id=str(a.doctor_id),
            scheduled_for=a.scheduled_for.isoformat()
        )
        for a in appointments
    ]
