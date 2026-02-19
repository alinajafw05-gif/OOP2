class Patient:
  def __init__(self, name, age, mrn="Temp-000", blood_type="Unknown"):
   self.mrn = mrn
   self.name = name
   self.age = age
   self.blood_type = blood_type
  def display_info(self):
   print(f"[{self.mrn}] {self.name} | Age: {self.age} | Type: {self.blood_type}")
p_standard = Patient("Sara Ahmed", 29, "REG-555", "A-")
p_emergency = Patient("John Doe", 40)
print("\n--- Activity 2 Results ---")
p_standard.display_info()
p_emergency.display_info()