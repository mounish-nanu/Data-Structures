# Basic Node template 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

        
# Parent class where the methods for basic operations are declared
class LinkedList: 
    def __init__(self):
        self.head = None  # initialize the head of the linked list

    # insertAtStart() method is defined to insert the element at the start which takes "data" as input 
    # which is the node value
    def insertAtStart(self, data):
        newNode = Node(data)  # we create a new node with the data

        if self.head is None:
            self.head = newNode  # if linked list is empty, we add the newNode to head
        else:
            newNode.next = self.head  # else we perform the following: assume there is a linked list with head->2->4
            self.head = newNode        # we are to insert 5
        return                          # step 1: (head, 5)->2->4 it means head and 5 points to 2
                                         # step 2: head->5->2->4 head is pointed to 5 and the rest remains
    
    # insertAtIndex() method is defined to insert the element at a particular index
    def insertAtIndex(self, index, data):
        newNode = Node(data)  # create a new node with the data
        if index == 0:
            self.insertAtStart(data)  # if index is 0, call insertAtStart
        i = 0
        current = self.head
        while (current is not None and i + 1 != index):
            i = i + 1
            current = current.next
        if current is not None:
            newNode.next = current.next  # link the new node to the next node
            current.next = newNode        # insert the new node in the list
        else:
            print("index not found")      # if the current node is None, index is out of bounds

    # insertAtEnd() method is defined to insert the element at the end of the list
    def insertAtEnd(self, data):
        newNode = Node(data)  # create a new node with the data

        if self.head is None:
            self.head = newNode  # if linked list is empty, we add the newNode to head

        current = self.head
        while (current.next is not None):
            current = current.next  # traverse to the last node

        current.next = newNode  # link the last node to the new node
        return
    
    # search() method is defined to search for a value in the linked list
    def search(self, data):
        if self.head is None:
            print("Linked list is empty")  # check if the linked list is empty
            return
        current = self.head
        index = 0

        while (current.next is not None):
            # print(current.value)  # optional: print current value during search
            if current.value == data:
                print("value found at index", + index)  # if value is found, print index
                return
            index += 1
            current = current.next  # move to the next node
            
        print("value not found in linked list")  # if we reach the end without finding the value
        return
    
    # printLL() method is defined to print the values of the linked list
    def printLL(self):
        self.length = 0  # initialize length to 0
        if self.head is None:
            print("Linked list is empty")  # check if the linked list is empty
        else:
            current = self.head
            while (current is not None):
                self.length += 1  # increment length for each node
                print(current.value)  # print the value of the current node
                current = current.next  # move to the next node

    # lengthOfLinkedList() method is defined to print the length of the linked list
    def lengthOfLinkedList(self):
        print(self.length)  # print the total length of the linked list


LL = LinkedList()  # create an instance of LinkedList
LL.insertAtStart(5)  # insert 5 at the start
LL.insertAtIndex(1, 6)  # insert 6 at index 1
LL.insertAtIndex(2, 7)  # insert 7 at index 2
LL.insertAtIndex(3, 30)  # insert 30 at index 3
LL.insertAtIndex(4, 31)  # insert 31 at index 4
LL.printLL()  # print the linked list
LL.search(5)  # search for the value 5 in the linked list
LL.lengthOfLinkedList()  # print the length of the linked list
