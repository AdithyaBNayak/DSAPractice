class Employee:
    no_of_leaves = 12
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position
    
    def __add__(self,other):
        return self.salary + other.salary
    
    def print_details(self):
        print("This is instance of class Employee")
    
    def __truediv__(self,other):
       return self.salary / other.salary
   
    def __repr__(self):
       return self.print_details()
   
    def __str__(self):
        return "This is Class Employee"  
        
adi = Employee("Adithya",700,"Software Engineer")
sumanyu = Employee("Sumanyu", 800, "Doctor")

print(adi + sumanyu)
print(adi/sumanyu)
print(adi)