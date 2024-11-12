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
    
    def search(self, data):
        if self.head is None:
            print("Linked list is empty")  # check if the linked list is empty
            return
        current = self.head
        index = 0

        while (current is not None):  # loop through each node
            if current.value == data:
                print("value found at index", + index)  # if value is found, print index
                return
            index += 1
            current = current.next  # move to the next node
            
        print("value not found in linked list")  # if we reach the end without finding the value
        return
    
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

    def lengthOfLinkedList(self):
        print(self.length)  # print the total length of the linked list

    def deleteAnElement(self, i):
        current = self.head  # start with the head of the list
        k = 0  # initialize index counter
        # Check if the list is empty
        if current is None:
            print("Linked list is empty")  # handle empty list case
            return

        # Traverse the list to find the node just before the one to delete
        if i == 0:
            self.head = current.next  # if deleting the head, update head to next node
            print("delete successful")  # confirm deletion
            return

        # Initialize previous node tracker
        prev = None  
        while (current is not None and k < i):
            prev = current  # keep track of the previous node
            current = current.next  # move to the next node
            k += 1  # increment index counter

        # If current is None, the index is out of bounds
        if current is None:
            print("index out of bounds")  # index not found case
        else:
            prev.next = current.next  # bypass the current node to delete it
            print("delete successful")  # confirm deletion
            self.printLL()  # print the updated linked list
    
    def reversingLL(self):
        previous = None
        current = self.head
        following = self.head
        while(current!=None):
            following = following.next
            current.next = previous
            previous = current
            current = following
        self.head = previous
        self.printLL() #print reversed linked list
        return previous
    


LL = LinkedList()  # create an instance of LinkedList
LL.insertAtStart(5)  # insert 5 at the start
LL.insertAtIndex(1, 6)  # insert 6 at index 1
LL.insertAtIndex(2, 7)  # insert 7 at index 2
LL.insertAtIndex(3, 30)  # insert 30 at index 3
LL.insertAtIndex(4, 31)  # insert 31 at index 4
LL.printLL()  # print the linked list
LL.search(5)  # search for the value 5 in the linked list
LL.lengthOfLinkedList()  # print the length of the linked list
LL.deleteAnElement(2)  # delete element at index 2
LL.reversingLL()
