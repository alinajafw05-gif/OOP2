class Patient:
    # Default values for mrn and blood_type
    def __init__(self, name, age, mrn="Temp-000", blood_type="Unknown"):
        self.mrn = mrn
        self.name = name
        self.age = age
        self.blood_type = blood_type

    def display_info(self):
        print(f"[{self.mrn}] {self.name} | Age: {self.age} | Type: {self.blood_type}")

    # Corrected update_name method
    def update_name(self, name):
        self.name = name  # FIX: Now we correctly update the object's name
        print(f"Inside method: Name changed to {name}")


# --- Testing the Correction ---
p3 = Patient("Ali", 25)
print(f"\nBefore Update: {p3.name}")

p3.update_name("Najaf")

print(f"After Update (Correct): {p3.name}")
