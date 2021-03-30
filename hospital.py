class Hospital():
    def __init__(self, capacity):
        self.bed_cap = capacity
        self.patients = []

    #method to check available beds
    def available_beds(self):
        return self.bed_cap - len(self.patients)

    #method to admit patient
    def admit_patient(self, name):
        if not self.available_beds():
            return False
        self.patients.append(name)
        return True

hospital1 = Hospital(3)

patient_list = ["Mike", "Jane", "Morris", "Kate"]

for patient in patient_list:
    if hospital1.admit_patient(patient):
        print(f"Admitted {patient} to the hospital")
    else:
        print(f"Failed to admit {patient} to the hospital. No Available Beds")