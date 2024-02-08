# type declaration for a linked list of integers: 

# Node of a Singly Linked List
class Node:
    # constructor
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
    # method for setting the data fields of the node
    def setData(self, data):
        self.data = data

    # method for getting the data fields of the node
    def getData(self):
        return self.data

    # method for setting the next field of the node
    def setNext(self, next):
        self.next = next

    # method for getting the next field of the node
    def getNext(self):
        return self.next
    
    # returns true if the node points to another node
    def hasNext(self):
        return self.next != None

# class for defining a linked list
class LinkedList(object):
    # initializing a list
    def __init__(self, node = None):
        self.length = 0
        self.head = node

    # Traversing the Linked List
    def ListLength(self):
        current = self.head
        count = 0
        while current != None:
            count = count+1
            current = current.next
        return count

my_linked_list = LinkedList()
print(my_linked_list.ListLength())