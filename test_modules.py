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
