# Class Methods
"""
Class methods can be applied on  both class and instance
"""

class Employee:
    no_of_leaves = 10

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

print(Employee.no_of_leaves)
adi = Employee()
print(adi.no_of_leaves)

print("\n\nUsing Instance")
adi.change_leaves(25)
print(adi.no_of_leaves)
print(Employee.no_of_leaves)

print("\n\nUsing Class")
Employee.change_leaves(35)
print(adi.no_of_leaves)
print(Employee.no_of_leaves)


print("\n\nYou can also give values to constructor using class metods")
class Employee:
    no_of_leaves = 10

    def __init__(self, name, salary, position):
        self.salary = salary
        self.name = name
        self.position = position

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_str(cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))
        # The aove line acts like *args
    
adi = Employee.from_str("Adithya-7-SOftware Engineer")
print(adi.name)
print(adi.salary)
print(adi.position)