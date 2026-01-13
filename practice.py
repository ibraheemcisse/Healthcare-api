patients = []

patients.append({"name": "John", "age": 30, "condition": "flu"})
patients.append({"name": "Jake", "age": 25, "condition": "checkup"})
patients.append({"name": "Suzy", "age": 45, "condition": "diabetes"})
patients.append({"name": "ibrahim", "age": 28, "condition": "allergy"})

print(f"Total patients: {len(patients)}")

for patient in patients:
    print(f"{patient['name']}, age {patient['age']}, visiting for: {patient['condition']}")

#filter - only patients older than 30 

print("\n--- Patients over 30 ---")
for patient in patients:
    if patient['age'] > 30:
        print(f"{patient['name']}, is {patient['age']} years old.")