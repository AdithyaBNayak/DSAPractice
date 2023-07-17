class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}.{lname}@company.com"
    
adi = Employee("Adithya","Bhairanje")
print(adi.email)

adi.fname = "Sumanyu"
print(adi.email)

"""
Inorder to avoid this issue we use a function 
        
"""

print("-------------------------------------------")

class Employee1:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{fname}.{lname}@company.com"
    
    def email(self):
        return  f"{self.fname}.{self.lname}@company.com" 
    
adi1 = Employee1("Adithya","Bhairanje")
print(adi1.email)
print(adi1.email())

adi1.fname = "Sumanyu"
print(adi1.email)
print(adi1.email())

"""
Inorder to avoid calling it like a function we use @property        
"""
print("-------------------------------------------")
class Employee2:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{fname}.{lname}@company.com"
    
    @property
    def email(self):
        return  f"{self.fname}.{self.lname}@company.com" 
    
adi2 = Employee2("Adithya","Bhairanje")
print(adi2.email)

adi2.fname = "Sumanyu"
print(adi2.email)
print("-------------------------------------------")


# adi2.email = "abc@compny.com"
# The above line givers us the error, You can set the value of that property outside

"""
Now imagine you want to set fname and lname based from provided email. You need to use setter
you can set a email, so that you can set the value for property from outside
"""
class Employee3:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{fname}.{lname}@company.com"
    
    def explain(self):
        return f"FName= {self.fname} and LName= {self.lname}"    
    
    @property
    def email(self):
        return  f"{self.fname}.{self.lname}@company.com"
    
    @email.setter
    def email(self,emailStr):
        full_name = emailStr.split("@")[0]
        names = full_name.split(".")
        self.fname = names[0]
        self.lname = names[1]
    
adi3 = Employee3("Adithya","Bhairanje")
print(adi3.email)

adi3.fname = "Sumanyu"
print(adi3.email)

print(adi3.explain())

adi3.email = "Akash.Rao@company.com"
print(adi3.explain())


print("-------------------------------------------")

"""
Imagine if you want to delete an element
"""

# del adi3.email
# This above code checks for deleter
class Employee4:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{fname}.{lname}@company.com"
    
    def explain(self):
        return f"FName= {self.fname} and LName= {self.lname}"    
    
    @property
    def email(self):
        if self.fname == None and self.lname == None:
            return "Email is not set"
            
        return  f"{self.fname}.{self.lname}@company.com"
    
    @email.setter
    def email(self,emailStr):
        full_name = emailStr.split("@")[0]
        names = full_name.split(".")
        self.fname = names[0]
        self.lname = names[1]
    
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None    
    
adi4 = Employee4("Adithya","Bhairanje")
print(adi4.email)

adi4.fname = "Sumanyu"
print(adi4.email)

print(adi4.explain())

adi4.email = "Akash.Rao@company.com"
print(adi4.explain())

del adi4.email

print(adi4.email) # None.None@company.com
# Thats why provide a if statement


print("-------------------------------------------")