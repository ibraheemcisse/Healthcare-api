import uuid
from datetime import datetime

def create_patient(name, age, condition):
    if not name:
        raise ValueError("Name cannot be empty")
    
    if not condition:
        raise ValueError("Condition cannot be empty")

    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a positive integer")

    patient = {
        "id": str(uuid.uuid4()),
        "name": name,
        "age": age,
        "condition": condition,
        "registered_at": datetime.now().isoformat()
    }
    return patient

# Test with negative age
try:
    patient1 = create_patient("Ibrahim", 25, "flu")
    print(patient1)
except ValueError as e:
    print(f"Error: {e}")

try:
    patient2 = create_patient("luke", 35, "checkup")
    print("\nValid patient created:")
    print(patient2)
except ValueError as e:
    print(f"Error: {e}")

try:
    patient3 = create_patient("Sara", 40, "Cancer")  # Empty condition
    print(patient3)
except ValueError as e:
    print(f"Error: {e}")
