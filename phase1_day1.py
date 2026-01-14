import uuid
import json
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

def save_patients_to_file(patients, filename="patients.json"):
    with open(filename, 'w') as f:
        json.dump(patients, f, indent=2)
    print(f"Saved {len(patients)} patients to {filename}")

def load_patients_from_file(filename="patients.json"):
    with open(filename, 'r') as f:
        patients = json.load(f)
    print(f"Loaded {len(patients)} patients from {filename}")
    return patients

# Create and save patients
patients = []
patients.append(create_patient("Ibrahim", 28, "checkup"))
patients.append(create_patient("Luke", 35, "flu"))
patients.append(create_patient("Sara", 42, "diabetes"))

save_patients_to_file(patients)

# Load patients back
print("\n--- Loading patients ---")
loaded_patients = load_patients_from_file()

for patient in loaded_patients:
    print(f"{patient['name']} (ID: {patient['id'][:8]}...)")