# Assignment Problem  11
# Class to implement Stack Using 2 Queues
class MyStack:
    # Creation of 2 queues
    def __init__(self):
        self.queue1 = []
        self.queue2 = []  

    # Pushing the element into the stack
    def push(self, data):                     #  <----- O(n)
        # We empty the queue1 to fill the queue2  
        while self.queue1:
            self.queue2.append(self.queue1.pop(0))
        # fill the incoming data into the queue1    
        self.queue1.append(data)
        # Then we empty the queue2 to fill queue1
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))

    # Popping the element out of the stack
    def pop(self):                         #  <------O(1)
        # if queue1 is  not empty , pop out its element
        if self.empty(): 
            print("The Stack is Empty")
        else: 
            return self.queue1.pop(0)     

    # To return the top element of the stack without popping it 
    def top(self):                        #   <-------O(1)
         # if queue1 is  not empty , return its top element without popping it
        if self.empty(): 
            print("The Stack is Empty")
        else: 
            return self.queue1[0]

    # Check if the stack is empty
    def empty(self):
        # if queue1 is empty return True, else False
        return False if self.queue1 else True

# Driver Code 

print("-------Scenario 1-------")
stack = MyStack()
stack.push(4)
stack.push(5)
stack.push(7)
print(stack.pop())
print(stack.pop())
print(stack.top())
print(stack.pop())
print(stack.empty())
print("--------------")

print("-------Scenario 2-------")
stack1 = MyStack()
stack1.push(4)
stack1.push(5)
stack1.push(7)
print(stack1.pop())
print(stack1.pop())
print(stack1.top())
print(stack1.empty())
print("--------------")
