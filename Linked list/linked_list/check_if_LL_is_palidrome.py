class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def is_palindrome(a):
    def middle_of_LL(a):
        fast = a
        slow = a
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def rev(start):
        prev = None
        current = start
        following = start

        while current != None:
            following = following.next
            current.next = prev
            prev = current
            current = following
        return prev
    
    middle = middle_of_LL(a)
    middle.next = rev(middle.next)

    current = middle.next

    while current != None:
        if a.value != current.value:
            return False
        current = current.next
        a = a.next
    return True


a = Node(1)
a.next = Node(2)
a.next.next = Node(1)
a.next.next.next = Node(3)
a.next.next.next.next = Node(1)
a.next.next.next.next.next = Node(2)
a.next.next.next.next.next.next = Node(1)

print(is_palindrome(a))
    


    

