import json

def load_patients_from_file(filename="patients.json"):
    with open(filename, 'r') as f:
        patients = json.load(f)
    return patients

def search_patient_by_name(patients, name):
    results = []
    for patient in patients:
        if name.lower() in patient['name'].lower():
            results.append(patient)
    return results

def filter_patients_by_age(patients, min_age):
    results = []
    for patient in patients:
        if patient['age'] >= min_age:
            results.append(patient)
    return results

def find_patient_by_id(patients, patient_id):
    for patient in patients:
        if patient['id'] == patient_id:
            return patient
    return None

def update_patient_condition(patients, patient_id, new_condition):
    for patient in patients:
        if patient['id'] == patient_id:
            patient['condition'] = new_condition
            return True
    return False

def delete_patient(patients, patient_id):
    for i, patient in enumerate(patients):
        if patient['id'] == patient_id:
            del patients[i]
            return True
    return False

# Load patients
patients = load_patients_from_file()

# Search for "Ibrahim"
results = search_patient_by_name(patients, "Ibrahim")

print(f"Found {len(results)} patient(s):")
for patient in results:
    print(f"- {patient['name']}, age {patient['age']}, {patient['condition']}")

# Filter patients over 30
print("\n--- Patients 30 and older ---")
older_patients = filter_patients_by_age(patients, 30)
for patient in older_patients:
    print(f"- {patient['name']}, age {patient['age']}")

# Get first patient's ID from the list
test_id = patients[0]['id']
print(f"\n--- Looking up patient {test_id[:8]}... ---")

found = find_patient_by_id(patients, test_id)
if found:
    print(f"Found: {found['name']}, {found['condition']}")
else:
    print("Patient not found")

# Update first patient's condition
test_id = patients[0]['id']
print(f"\n--- Updating patient {test_id[:8]}... ---")
updated = update_patient_condition(patients, test_id, "recovered")
if updated:
    print(f"Updated condition to: {patients[0]['condition']}")

# Delete last patient
deleted_id = patients[-1]['id']
print(f"\n--- Deleting patient {deleted_id[:8]}... ---")
deleted = delete_patient(patients, deleted_id)
print(f"Remaining patients: {len(patients)}")