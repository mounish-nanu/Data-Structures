class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def sum_of_lists(a,b):
    current1 = a
    sr1 = ""
    while current1 != None:
        sr1 += str((current1.value))
        current1 = current1.next

    m = int(sr1)

    current2 = b
    sr2 = ""
    while current2 != None:
        sr2 += str((current2.value))
        current2 = current2.next
    
    n = int(sr2)
    
    def rev(x):
        current = x
        prev = None
        following = x
        while(current!=None):
            following = following.next
            current.next = prev
            prev = current
            current = following
        return prev

    k = m + n
    d = Node(0)
    current = d
    while k//10 != 0:
        t = Node(k%10)
        current.next = t
        current = current.next
        k = k//10
    current.next = Node(k)
    x = d.next
    head = rev(x)

    while head != None:
        print(head.value)
        head = head.next

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)

b = Node(9)
b.next = Node(9)
b.next.next = Node(9)

sum_of_lists(a,b)
    

    



    



