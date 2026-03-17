from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/patients")
async def list_patients():
    with open("patients.json", "r") as f:
        return json.load(f)

@router.post("/appointments")
async def create_appointment(patient_id: str, doctor_id: str, date: str):
    pass
