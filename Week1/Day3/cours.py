class Employee:
    def __init__(self, firstname, lastname, age, job, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary

    def get_fullname(self):
        return self.firstname + self.lastname
    def happy_birthday(self):
        self.age += 1
        return self.age
    def get_promotion(self, promotion_amount):
        self.salary += promotion_amount
    def show_info(self):
        print("f {self.get_fullname} is {self.age} years old, works as a {self.job} and earns {self.salary} per month.")    
        
    
Employee1 = Employee("Lea", "Smith", 30, "Software Developer", 5000)
Employee2 = Employee("John", "Doe", 25, "Graphic Designer", 4000)

Employee1.get_promotion (1000)
Employee1.happy_birthday()
Employee2.show_info()