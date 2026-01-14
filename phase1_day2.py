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