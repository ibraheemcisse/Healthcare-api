"""
FastAPI application entry point.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.registry import PatientRegistry

# Create FastAPI instance
app = FastAPI(
    title="Healthcare Appointment API",
    description="API for managing patient appointments",
    version="0.1.0"
)

# Initialize patient registry
registry = PatientRegistry()

# Pydantic models for request/response validation
class PatientCreate(BaseModel):
    name: str = Field(..., min_length=1, description="Patient's full name")
    age: int = Field(..., ge=0, le=150, description="Patient's age")
    condition: str = Field(..., min_length=1, description="Medical condition")

class PatientResponse(BaseModel):
    id: str
    name: str
    age: int
    condition: str
    registered_at: str

@app.get("/")
def root():
    """Root endpoint - API info"""
    return {
        "service": "Healthcare Appointment API",
        "version": "0.1.0",
        "status": "running"
    }

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "healthcare-api"
    }

@app.post("/patients", response_model=PatientResponse, status_code=201)
def create_patient(patient: PatientCreate):
    """Create a new patient"""
    try:
        new_patient = registry.add_patient(
            name=patient.name,
            age=patient.age,
            condition=patient.condition
        )
        return new_patient
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/patients")
def list_patients():
    """Get all patients"""
    return {
        "total": registry.get_count(),
        "patients": registry.get_all()
    }

@app.get("/patients/{patient_id}")
def get_patient(patient_id: str):
    """Get patient by ID"""
    patient = registry.find_by_id(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

# Appointment models
class AppointmentCreate(BaseModel):
    patient_id: str = Field(..., description="Patient UUID")
    doctor_id: str = Field(..., description="Doctor UUID")
    days_from_now: int = Field(..., ge=1, le=365, description="Days in future to schedule")

class AppointmentResponse(BaseModel):
    patient_id: str
    doctor_id: str
    scheduled_for: str
    days_away: int

@app.post("/appointments", response_model=AppointmentResponse, status_code=201)
def create_appointment(appointment: AppointmentCreate):
    """Schedule an appointment for a patient"""
    # Verify patient exists
    patient = registry.find_by_id(appointment.patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    # Schedule appointment
    updated_patient = registry.schedule_appointment(
        patient_id=appointment.patient_id,
        days_from_now=appointment.days_from_now,
        doctor_id=appointment.doctor_id
    )
    
    if not updated_patient or 'appointment' not in updated_patient:
        raise HTTPException(status_code=500, detail="Failed to schedule appointment")
    
    return {
        "patient_id": appointment.patient_id,
        "doctor_id": appointment.doctor_id,
        "scheduled_for": updated_patient['appointment']['scheduled_for'],
        "days_away": updated_patient['appointment']['days_away']
    }

@app.get("/doctors/{doctor_id}/schedule")
def get_doctor_schedule(doctor_id: str):
    """Get all appointments for a doctor"""
    appointments = registry.get_appointments_by_doctor(doctor_id)
    return {
        "doctor_id": doctor_id,
        "total_appointments": len(appointments),
        "appointments": appointments
    }
