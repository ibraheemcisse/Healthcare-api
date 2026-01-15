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
    
    def filter_by_age(self, min_age=None, max_age=None):
        results = []
        for patient in self.patients:
            if (min_age is None or patient['age'] >= min_age) and (max_age is None or patient['age'] <= max_age):
                results.append(patient)
        return results
    
    def filter_by_id(self, patient_id):
        for patient in self.patients:
            if patient['id'] == patient_id:
                return patient
        return None
    
    def get_count(self):
        return len(self.patients)
    
    def save_to_file(self, filename="patients.json"):
        try:
            with open(filename, 'w') as f:
                json.dump(self.patients, f, indent=2)
            print(f"✓ Saved {len(self.patients)} patients")
            return True
        except OSError as e:
            print(f"✗ Error saving: {e}")
            return False
    
    def load_from_file(self, filename="patients.json"):
        try:
            with open(filename, 'r') as f:
                self.patients = json.load(f)
            print(f"✓ Loaded {len(self.patients)} patients")
            return True
        except FileNotFoundError:
            print(f"✗ File not found")
            return False
        except json.JSONDecodeError:
            print(f"✗ Invalid JSON")
            return False

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

print("\n--- Patient by 30+ ---")
older = clinic.filter_by_age(min_age=30)
for p in older:
    print(f"Older patient: {p['name']}, {p['age']}")

# Save current patients
print("\n--- Saving ---")
clinic.save_to_file("clinic_data.json")

# Create new clinic and load
print("\n--- Loading into new clinic ---")
new_clinic = PatientRegistry()
new_clinic.load_from_file("clinic_data.json")
print(f"New clinic has {new_clinic.get_count()} patients")

print(f"\nTotal {clinic.get_count()} patients")