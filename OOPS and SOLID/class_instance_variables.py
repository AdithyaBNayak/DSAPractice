"""
Class Variables and Instance Variables
You can access Class Variables from Instnace and Class
You can modify Class Variables only from Class and not from Instance
"""

class Student:
    school = "MKS"

adi = Student()
sumanyu = Student()

adi.name = "AdithyaB"
sumanyu.name = "Sumanyu SS Acharya"

adi.grade = 10
sumanyu.grade = 9

print("Instance variables are listed below:")
print(adi.__dict__)
print(sumanyu.__dict__)

print("\n Class Variable is listed Below")
print(Student.school)
print(adi.school)
print(sumanyu.school)
print(adi.__dict__)
print(sumanyu.__dict__)

print("\nIf you change Class Variable:")
Student.school = "Lil ROck"
print(adi.school)
print(sumanyu.school)
print(adi.__dict__)
print(sumanyu.__dict__)

print("\nClass Variable will have same value even if you try to change it to a instance variable:")
adi.school = "Vidyodaya"
sumanyu.school = "Jnana Sudha"
print("Class Variable", Student.school)
print(adi.school)
print(sumanyu.school)
print(adi.__dict__)
print(sumanyu.__dict__)