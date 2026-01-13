import uuid
from datetime import datetime

# Create patient with unique ID and timestamp
def create_patient(name, age, condition):
    patient = {
        "id": str(uuid.uuid4()),  # Generate unique ID
        "name": name,
        "age": age,
        "condition": condition,
        "registered_at": datetime.now().isoformat()  # ISO format timestamp
    }
    return patient

# Test it
patient1 = create_patient("Ibrahim", 28, "checkup")
patient2 = create_patient("mark", 35, "flu")

print(patient1)
print(patient2)
