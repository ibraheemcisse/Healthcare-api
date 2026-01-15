"""
Patient registry management.

This module provides the PatientRegistry class for managing patient records,
including CRUD operations, search, and file persistence.
"""

import json
from datetime import datetime, timedelta
from app.models import create_patient_dict


class PatientRegistry:
    """
    Manages a collection of patient records.
    
    Provides methods for adding, searching, filtering, and persisting
    patient data to JSON files.
    
    Attributes:
        patients (list): List of patient dictionaries
    """
    
    def __init__(self):
        """Initialize empty patient registry."""
        self.patients = []
    
    def add_patient(self, name, age, condition):
        """
        Add a new patient to the registry.
        
        Args:
            name (str): Patient name
            age (int): Patient age
            condition (str): Medical condition
        
        Returns:
            dict: The created patient record
        
        Raises:
            ValueError: If validation fails
        """
        patient = create_patient_dict(name, age, condition)
        self.patients.append(patient)
        return patient
    
    def get_all(self):
        """Get all patients."""
        return self.patients
    
    def get_count(self):
        """Get total number of patients."""
        return len(self.patients)
    
    def find_by_id(self, patient_id):
        """Find patient by exact ID match."""
        for patient in self.patients:
            if patient['id'] == patient_id:
                return patient
        return None
    
    def search_by_name(self, name):
        """Search patients by partial name match (case-insensitive)."""
        return [p for p in self.patients if name.lower() in p['name'].lower()]
    
    def filter_by_age(self, min_age):
        """Filter patients by minimum age."""
        return [p for p in self.patients if p['age'] >= min_age]
    
    def get_patients_by_condition(self, condition):
        """Get all patients with specific condition (case-insensitive)."""
        return [p for p in self.patients if p['condition'].lower() == condition.lower()]
    
    def schedule_appointment(self, patient_id, days_from_now):
        """
        Schedule an appointment for a patient.
        
        Args:
            patient_id (str): Patient UUID
            days_from_now (int): Number of days in future
        
        Returns:
            dict: Updated patient with appointment, or None if not found
        """
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
        """Save all patients to JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.patients, f, indent=2)
            return True
        except OSError:
            return False
    
    def load_from_file(self, filename="patients.json"):
        """Load patients from JSON file."""
        try:
            with open(filename, 'r') as f:
                self.patients = json.load(f)
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            return False
