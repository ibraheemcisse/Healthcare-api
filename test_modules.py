from app.registry import PatientRegistry

# Test the modular code
clinic = PatientRegistry()

# Add patients
clinic.add_patient("Ibrahim", 28, "checkup")
clinic.add_patient("Luke", 35, "flu")
clinic.add_patient("Sara", 42, "diabetes")

# Test methods
print(f"Total patients: {clinic.get_count()}")
print("\nAll patients:")
for p in clinic.get_all():
    print(f"- {p['name']}, {p['age']}, {p['condition']}")

print("\n30+ years old:")
for p in clinic.filter_by_age(30):
    print(f"- {p['name']}, {p['age']}")

print("\nSearching for 'Luke':")
for p in clinic.search_by_name("Luke"):
    print(f"- {p['name']}")

# Test utility functions
from app.utils import format_patient_summary, calculate_age_from_birthdate

print("\n--- Formatted summaries ---")
for p in clinic.get_all():
    print(format_patient_summary(p))

# Test age calculation
print("\n--- Age from birthdate ---")
birthdate = "1995-03-15T00:00:00"  # March 15, 1995
age = calculate_age_from_birthdate(birthdate)
print(f"Born {birthdate[:10]}, age: {age}")

# Test utility functions
from app.utils import format_patient_summary, calculate_age_from_birthdate

print("\n--- Formatted summaries ---")
for p in clinic.get_all():
    print(format_patient_summary(p))

# Test age calculation
print("\n--- Age from birthdate ---")
birthdate = "1995-03-15T00:00:00"  # March 15, 1995
age = calculate_age_from_birthdate(birthdate)
print(f"Born {birthdate[:10]}, age: {age}")
