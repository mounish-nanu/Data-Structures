class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList: 
    def __init__(self):
        self.head = None  # initialize the head of the linked list

    def insertAtStart(self, data):
        newNode = Node(data)  # create a new node with the data

        if self.head is None:
            self.head = newNode  # if linked list is empty, we add the newNode to head
        else:
            newNode.next = self.head  # link newNode to the current head
            self.head = newNode        # update head to point to newNode
        return  # end of insertAtStart method
    
    def insertAtIndex(self, index, data):
        newNode = Node(data)  # create a new node with the data
        if index == 0:
            self.insertAtStart(data)  # if index is 0, call insertAtStart
            return  # end of insertAtIndex if inserted at start
        i = 0
        current = self.head
        while (current is not None and i + 1 != index):
            i += 1  # increment index
            current = current.next  # move to next node
        if current is not None:
            newNode.next = current.next  # link the new node to the next node
            current.next = newNode        # insert the new node in the list
        else:
            print("index not found")      # if the current node is None, index is out of bounds

    def insertAtEnd(self, data):
        newNode = Node(data)  # create a new node with the data

        if self.head is None:
            self.head = newNode  # if linked list is empty, we add the newNode to head

        current = self.head
        while (current.next is not None):
            current = current.next  # traverse to the last node

        current.next = newNode  # link the last node to the new node
        return  # end of insertAtEnd method
    
    def printLL(self):
        self.length = 0  # initialize length to 0
        if self.head is None:
            print("Linked list is empty")  # check if the linked list is empty
        else:
            current = self.head
            while (current is not None):  # loop through each node
                self.length += 1  # increment length for each node
                print(current.value)  # print the value of the current node
                current = current.next  # move to the next node
    
    def enqueue(self,data):
        current = self.head
        newNode = Node(data)
        while(current.next is not None):
            current = current.next
        current.next = newNode

    def dequeue(self):
        current = self.head
        self.head = self.head.next
        current.next = None

    

LL = LinkedList()  # create an instance of LinkedList
LL.insertAtStart(5)  # insert 5 at the start
LL.insertAtIndex(1, 6)  # insert 6 at index 1
LL.insertAtIndex(2, 7)  # insert 7 at index 2
LL.insertAtIndex(3, 30)  # insert 30 at index 3
LL.insertAtIndex(4, 31)  # insert 31 at index 4
LL.printLL()  # print the linked list
LL.dequeue()
LL.dequeue()
LL.printLL()
LL.enqueue(32)
LL.printLL()

