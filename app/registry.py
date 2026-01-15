import json
from datetime import datetime, timedelta
from app.models import create_patient_dict

class PatientRegistry:
    def __init__(self):
        self.patients = []
    
    def add_patient(self, name, age, condition):
        patient = create_patient_dict(name, age, condition)
        self.patients.append(patient)
        return patient
    
    def get_all(self):
        return self.patients
    
    def get_count(self):
        return len(self.patients)
    
    def find_by_id(self, patient_id):
        for patient in self.patients:
            if patient['id'] == patient_id:
                return patient
        return None
    
    def search_by_name(self, name):
        return [p for p in self.patients if name.lower() in p['name'].lower()]
    
    def filter_by_age(self, min_age):
        return [p for p in self.patients if p['age'] >= min_age]
    
    def get_patients_by_condition(self, condition):
        return [p for p in self.patients if p['condition'].lower() == condition.lower()]
    
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
    
    def save_to_file(self, filename="patients.json"):
        try:
            with open(filename, 'w') as f:
                json.dump(self.patients, f, indent=2)
            return True
        except OSError:
            return False
    
    def load_from_file(self, filename="patients.json"):
        try:
            with open(filename, 'r') as f:
                self.patients = json.load(f)
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            return False
