from fastapi import APIRouter

router = APIRouter()

@router.get("/patients")
async def list_patients():
    pass
