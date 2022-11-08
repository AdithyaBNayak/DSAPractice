# Defining a class to implement Queue using 2 stacks
class MyQueue:
    def __init__(self):
        # Initialise 2 stacks
        self.stack1 = []
        self.stack2 = []
    
    # Push an element into the Queue
    def push(self, data):
        # Internally we push the element into the first stack
        self.stack1.append(data)
        
    # Pop an element out of the queue
    def pop(self):
        # Fill in the stack 2 by popping out the elements from stack1
        self.processQueue()  
        # pop out the element from the stack 2    
        return self.stack2.pop()

    def empty(self):
        # Fill in the stack 2 by popping out the elements from stack1
        self.processQueue()
        # if stack2 is empty return True, else False
        return False if self.stack2 else True
            
    # Return the first inserted element if queue is not empty 
    def peek(self):
        # Fill in the stack 2 by popping out the elements from stack1
        self.processQueue() 
        # Return the first inserted element if stack2 is not empty       
        if self.empty():
            print("Queue is empty")
        else:    
            return self.stack2[-1]

    # Function feeds the element from stack1 to stack2
    def processQueue(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

# Driver Code
print("################")   
print("Scenario 1 : ")
queue = MyQueue()
queue.push(2)
queue.push(3)
print(queue.pop())
print(queue.peek())
if queue.empty():
    print("Queue is empty")
else:
    print("Queue is not empty")
print("################")    

print("\n################")   
print("Scenario 2 : ")
queue = MyQueue()
queue.push(7)
queue.push(6)
print(queue.pop())
print(queue.peek())
print(queue.pop())
if queue.empty():
    print("Queue is empty")
else:
    print("Queue is not empty")
print("################")  

