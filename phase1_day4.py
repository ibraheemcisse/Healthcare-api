import uuid
import json
from datetime import datetime

class PatientRegistry:
    def __init__(self):
        self.patients = []
    
    def add_patient(self, name, age, condition):
        # Validation
        if not name:
            raise ValueError("Name cannot be empty")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a positive integer")
        if not condition:
            raise ValueError("Condition cannot be empty")
        
        # Create patient
        patient = {
            "id": str(uuid.uuid4()),
            "name": name,
            "age": age,
            "condition": condition,
            "registered_at": datetime.now().isoformat()
        }
        self.patients.append(patient)
        return patient
    
    def search_by_name(self, name):
        results = []
        for patient in self.patients:
            if name.lower() in patient['name'].lower():
                results.append(patient)
        return results

# Test it
clinic = PatientRegistry()
patient1 = clinic.add_patient("Ibrahim", 28, "checkup")
patient2 = clinic.add_patient("Luke", 35, "flu")

print(f"Total patients in clinic: {len(clinic.patients)}")
for p in clinic.patients:
    print(f"- {p['name']}, {p['age']}")

print("\n--- Searching for 'Luke' ---")
results = clinic.search_by_name("Luke")
for p in results:
    print(f"Found: {p['name']}, {p['condition']}")