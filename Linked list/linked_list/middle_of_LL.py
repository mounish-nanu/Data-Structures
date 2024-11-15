class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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
            print("index not found")
    
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
        print(self.length)
        
    def middle(self):
        A = self.head
        B = self.head

        while(B is not None and B.next is not None):
            A = A.next
            B = (B.next).next
        
        return A.value

    
    
LL = LinkedList()
LL.insertAtIndex(0, 5) 
LL.insertAtIndex(1, 6)  
LL.insertAtIndex(2, 7)  
LL.insertAtIndex(3, 30) 
LL.insertAtIndex(4, 31)
LL.insertAtIndex(5, 32)
LL.printLL()
print(LL.middle())
# LL.lengthOfLinkedList()