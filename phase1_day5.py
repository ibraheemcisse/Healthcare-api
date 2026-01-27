import uuid
import json
from datetime import datetime, timedelta

class PatientRegistry:
    def __init__(self):
        self.patients = []
    
    def add_patient(self, name, age, condition):
        if not name or not condition:
            raise ValueError("Name and condition required")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be positive integer")
        
        patient = {
            "id": str(uuid.uuid4()),
            "name": name,
            "age": age,
            "condition": condition,
            "registered_at": datetime.now().isoformat()
        }
        self.patients.append(patient)
        return patient
    
    def filter_by_age_old(self, min_age):
        results = []
        for patient in self.patients:
            if patient['age'] >= min_age:
                results.append(patient)
        return results
    
    def filter_by_age(self, min_age):
        return [p for p in self.patients if p['age'] >= min_age]
    
    def schedule_appointment(self, patient_id, days_from_now):
        patient = self.find_by_id(patient_id)
        if not patient:
            return None
        
        appointment_date = datetime.now() + timedelta(days=days_from_now)
        patient['appointment'] = {
            "scheduled_for": appointment_date.isoformat(),
            "days_away": days_from_now
        }
        return patient
    
    def find_by_id(self, patient_id):
        for patient in self.patients:
            if patient['id'] == patient_id:
                return patient
        return None
    
    def get_all_names(self):
        return [p['name'] for p in self.patients]
    
    def get_patients_by_condition(self, condition):
        return [p for p in self.patients if p['condition'].lower() == condition.lower()]
    
    def get_average_age(self):
        if not self.patients:
            return 0
        total_age = sum(p['age'] for p in self.patients)
        return total_age / len(self.patients)

# Test
clinic = PatientRegistry()
clinic.add_patient("Ibrahim", 28, "checkup")
clinic.add_patient("Luke", 35, "flu")
clinic.add_patient("Sara", 42, "diabetes")

print("Old way:")
print(clinic.filter_by_age_old(30))

print("\nNew way (list comprehension):")
print(clinic.filter_by_age(30))

# Schedule appointment
patient_id = clinic.patients[0]['id']
print(f"\n--- Scheduling appointment ---")
clinic.schedule_appointment(patient_id, 3)

patient = clinic.find_by_id(patient_id)
if patient.get('appointment'):
    print(f"{patient['name']}'s appointment: {patient['appointment']['scheduled_for'][:10]}")
    print(f"In {patient['appointment']['days_away']} days")

# Test new methods
print("\n--- All patient names ---")
print(clinic.get_all_names())

print("\n--- Patients with flu ---")
flu_patients = clinic.get_patients_by_condition("flu")
for p in flu_patients:
    print(f"- {p['name']}")

print(f"\n--- Average age ---")
print(f"{clinic.get_average_age():.1f} years")touch app/__init__.py
