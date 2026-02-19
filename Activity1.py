class Patient:
    def __init__(self,name,age,mrn):
        self.name = name
        self.age = age
        self.mrn = mrn
    def display_info(self):
        print ("Name:",self.name)
        print ("Age:",self.age)
        print ("MRN:",self.mrn)


p1 = Patient("Ali",24,101)
p1.display_info()