import json

def load_patients_from_file(filename="patients.json"):
    try:
        with open(filename, 'r') as f:
            patients = json.load(f)
        print(f"✓ Loaded {len(patients)} patients")
        return patients
    except FileNotFoundError:
        print(f"✗ File {filename} not found. Returning empty list.")
        return []
    except json.JSONDecodeError:
        print(f"✗ Error decoding JSON from {filename}. Returning empty list.")
        return []
    
print("\n--- Testing corrupted JSON ---")
patients2 = load_patients_from_file("corrupted.json")
print(patients2)

def save_patients_to_file(patients, filename="patients.json"):
    try:
        with open(filename, 'w') as f:
            json.dump(patients, f, indent=2)
        print(f"✓ Saved {len(patients)} patients to {filename}")
        return True
    except (IOError, PermissionError) as e:
        print(f"✗ Error saving to {filename}: {e}")
        return False

# Test loading non-existent file
patients = load_patients_from_file("missing.json")
print(patients)

# Test saving to invalid location
print("\n--- Testing save error ---")
test_patients = [{"name": "Test", "age": 30}]
success = save_patients_to_file(test_patients, "/root/denied.json")
print(f"Save successful: {success}")