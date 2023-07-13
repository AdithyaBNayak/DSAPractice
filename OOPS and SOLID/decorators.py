"""
Decorators allow us to wrap another function in order to 
extend the behaviour of the wrapped function, 
without permanently modifying it. 

They can add logging or instrumentation code and extract various metrics such as timing 
from application components in an encapsulated manner.

Decorators can be the perfect mechanism to validate input, 
which is especially important when working in dynamically typed languages like Python.
"""



def function1():
    print("Inside Function 1")

func2 = function1
del function1
func2()

#  The above code still prints the statement even after deleting function1


print("\n\n\nBelow is the Decorator Example")
print("--------------------------------------")

def decor(baseFunc):
    def execute():
        print("Before Execution")
        baseFunc()
        print("After Execution")
    return execute

def mainFunc():
    print("Inside the Main Function")

execution = decor(mainFunc)
execution()

print("\n\n\nBelow is the Decorator with annotation")
print("--------------------------------------")
def wrap2(func):
    def decorate2():
        print("BEFORE")
        func()
        print("AFTER")
    return decorate2

@wrap2
def mainFunc2():
    print("Inside main function")

# Line which decorates will be replaces with annotation
mainFunc2()


"""
print("\n\n\nGFG Exmaple")
print("--------------------------------------")


@gfg_decorator
def hello_decorator():
    print("Gfg")

'''Above code is equivalent to -

def hello_decorator():
    print("Gfg")
    
hello_decorator = gfg_decorator(hello_decorator)'''

"""


"""
# CHaining of decorators

# code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner
 
def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner
 
@decor1
@decor
def num():
    return 10
 
@decor
@decor1
def num2():
    return 10
   
print(num()) ----------->400
print(num2())-----------> 200




"""