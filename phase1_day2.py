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

# Load patients
patients = load_patients_from_file()

# Search for "Ibrahim"
results = search_patient_by_name(patients, "Ibrahim")

print(f"Found {len(results)} patient(s):")
for patient in results:
    print(f"- {patient['name']}, age {patient['age']}, {patient['condition']}")
