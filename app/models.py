import uuid
from datetime import datetime

def create_patient_dict(name, age, condition):
    """Create a patient dictionary with validation"""
    if not name:
        raise ValueError("Name cannot be empty")
    if not condition:
        raise ValueError("Condition cannot be empty")
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be positive integer")
    
    return {
        "id": str(uuid.uuid4()),
        "name": name,
        "age": age,
        "condition": condition,
        "registered_at": datetime.now().isoformat()
    }
