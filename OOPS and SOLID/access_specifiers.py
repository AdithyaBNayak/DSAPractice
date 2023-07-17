# Access Specifiers
"""
Public
Private -  double underscore (Can be used only inside the class)
Protected - single underscore (Can be accessed in the class and in child classes)

"""
class Person:
    gender = "Male"
    _orientation = "Straight"
    __height = "124cm"

class Male(Person):
    _username = "Adithya"
    __password = "password123"
    name = "Adi B"

adi = Person()
print("\nInitial ADI")
print("-----------")
print(adi.gender)
print(adi._orientation)
print(adi._Person__height) # Toget Private variables value

print("\nFinal ADI")
print("-----------")
adi.gender = "MALE"
adi._orientation  = "STRAIGHT"
adi.__height= "132 cm"
print(adi.gender)
print(adi._orientation) 
print(adi._Person__height)  # Not Updated

print("\nINITIAL MAle")
print("-----------")

adithya = Male()
print(adithya.gender)
print(adithya._orientation)
print(adithya._Person__height) 

print(adithya.name)
print(adithya._username)
print(adithya._Male__password)     

print("\nFinal MAle")
print("-----------")
adithya.gender = "MALE"
adithya._orientation  = "STRAIGHT"
adithya.__height= "132 cm"
adithya.name = "ADITHYA"
adithya._username = "ADITHYAGDDHD"
adithya.__password = "dafafafs"

print(adithya.gender)
print(adithya._orientation)
print(adithya._Person__height) # Not Updated

print(adithya.name)
print(adithya._username)
print(adithya._Male__password) # Not Updated

