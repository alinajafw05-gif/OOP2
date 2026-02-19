class Patient:
    def __init__(self, name, age, mrn):
        self.__name = name
        self.__age = age
        self.__mrn = mrn

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age   

    def get_mrn(self):
        return self.__mrn

    # Activity 03: Setter with validation
    def set_age(self, new_age):
        if new_age > 0 and new_age < 120:
            self.__age = new_age
            print(f"Success: Age updated to {self.__age}")
        else:
            print(f"Error: {new_age} is not a valid age.")


p1 = Patient("Najaf", 12, 203)

print("Final Age:", p1.get_age())

p1.set_age(-5)     # invalid
p1.set_age(120)    # invalid
p1.set_age(46)     # valid

print(f"New Age: {p1.get_age()}")

