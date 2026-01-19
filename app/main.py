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
