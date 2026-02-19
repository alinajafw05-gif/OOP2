class Patient:
    def __init__(self, mrn, name, age, blood_type):
        self.mrn = mrn
        self.name = name
        self.age = age
        self.blood_type = blood_type
        print(f"Patient {self.name} created successfully.")

    def display_info(self):
        print(f"[{self.mrn}] {self.name} | Age: {self.age} | Type: {self.blood_type}")


p1 = Patient("101", "Ali Khan", 34, "O+")
p1.display_info()


