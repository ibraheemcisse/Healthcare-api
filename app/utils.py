from datetime import datetime

def format_patient_summary(patient):
    """Format patient info for display"""
    return f"{patient['name']} (age {patient['age']}) - {patient['condition']}"

def calculate_age_from_birthdate(birthdate_str):
    """Calculate age from ISO format birthdate"""
    birthdate = datetime.fromisoformat(birthdate_str)
    today = datetime.now()
    age = today.year - birthdate.year
    
    # Adjust if birthday hasn't happened this year
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age -= 1
    
    return age

def days_until_appointment(appointment_date_str):
    """Calculate days until appointment"""
    appointment = datetime.fromisoformat(appointment_date_str)
    now = datetime.now()
    delta = appointment - now
    return delta.days
