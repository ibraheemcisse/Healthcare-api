from fastapi import APIRouter

router = APIRouter()

@router.get("/patients")
async def list_patients():
    pass

@router.delete("/patients/{patient_id}")
async def delete_patient(patient_id: str):
    with open("patients.json", "r") as f:
        patients = json.load(f)
    patients = [p for p in patients if p["id"] != patient_id]
    with open("patients.json", "w") as f:
        json.dump(patients, f)
    return {"deleted": patient_id}
