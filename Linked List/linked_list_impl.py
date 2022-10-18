# This class defines a Node
class Node:
    # initialization of data and pointer
    def __init__(self,data):
        self.data = data 
        self.next =  None

# This class defines a LinkedList  
class LinkedList:
    # Initialization of head pointer
    def __init__(self):
        self.head = None 
        
    # Function definition to print the linked list
    def printLinkedList(self):
        temp = self.head
        # iterating through each node 
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
    
    # Function definition to add a node at the start of the linked list 
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # Function definition to add a node at the end of the linked list
    def insertAtEnd(self, new_data):
        temp = self.head
        new_node = Node(new_data)
        
        # if the linked list is empty, set the new node  to head pointer
        if temp is None:
            self.head = new_node
            return
        
        # iterate till the last node 
        while temp.next is not None:
            temp = temp.next
            
        temp.next = new_node    
    
    # Function definition to insert a node after the given node
    def insertAfterNode(self, prev_node, new_data):
        # If no node is provided
        if prev_node is None:
            print("Provoide a valid node")
            
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
            
            
# Driver Code 
llist =  LinkedList()
llist.insertAtEnd(29)
llist.insertAtEnd(50)
llist.insertAtBeginning(67)
llist.insertAfterNode(llist.head.next,65)
llist.printLinkedList()
