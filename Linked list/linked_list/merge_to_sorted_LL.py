class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LL :

    def merge_sorted_LL(self,a,b):
        current1 = a
        current2 = b
        self.newhead = Node(0)
        temp = self.newhead

        while (current1 and current2):
            if current1.value <= current2.value :
                temp.next = current1
                temp = current1
                current1 = current1.next
            else:
                temp.next = current2
                temp = current2
                current2 = current2.next
        if current1 != None:
            while current1:
                temp.next = current1
                current1 = current1.next
        elif current2 != None:
            while current2 :
                temp.next = current2
                current2 = current2.next
        
        return self.newhead.next
    
    def printLL(self,c):
        length = 0  # initialize length to 0
        if c is None:
            print("Linked list is empty")  # check if the linked list is empty
        else:
            current = c
            while (current is not None):  # loop through each node
                length += 1  # increment length for each node
                print(current.value)  # print the value of the current node
                current = current.next  # move to the next node
            


a = Node(2)
a.next = Node(4)
a.next.next = Node(8)
a.next.next.next = Node(9)


b = Node(1)
b.next = Node(3)
b.next.next = Node(8)
b.next.next.next = Node(10)

ob1 = LL()
c = ob1.merge_sorted_LL(a,b)
ob1.printLL(c)