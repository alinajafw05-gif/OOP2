from datetime  import datetime
class employee:
    def __init__(self,name,date_of_birth,qualification,department,date_of_joining):
        self.name=name
        self.date_of_birth=date_of_birth
        self.qualification=qualification
        self.department=department
        self.date_of_joining=date_of_joining
    def getServiceLen(self,curyear):
        curdate= datetime.today()
        return curdate - self.date_of_joining
    hiring_date = datetime(2020, 5, 17)
emp1=employee("John Doe",datetime(1990,4,25),"MSc Computer Science","IT",hiring_date)
service_length = emp1.getServiceLen(datetime.now().year)
print(f"Service Length of {emp1.name}: {service_length.days} days")
