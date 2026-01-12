patients = []

patients.append({"name": "John", "age": 30, "condition": "flu"})
patients.append({"name": "Jake", "age": 25, "condition": "checkup"})
patients.append({"name": "Suzy", "age": 45, "condition": "diabetes"})

print(f"Total patients: {len(patients)}")

for patient in patients:
    print(f"{patient['name']}, age {patient['age']}, visiting for: {patient['condition']}")

