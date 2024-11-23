class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

        
def reverse_k_group(a,value):
    if a is None or value <= 1:
        return a
    def rev(start , end):
        current = start
        prev = None
        while(current != end):
            following = current.next
            current.next = prev
            prev = current
            current = following
        return prev

    dummy = Node(0)
    dummy.next = a
    prev_grp_end = dummy
    current = a
            
    while current:
        k = 0
        group_start = current
        while current and k < value:
            current = current.next
            k = k + 1
        if k == value:
            new_grp = rev(group_start,current)
            prev_grp_end.next = new_grp
            prev_grp_end = group_start
        else:
            prev_grp_end.next = rev(group_start,current)
    return dummy.next

        
    
def printLL(a):
        length = 0  # initialize length to 0
        if a is None:
            print("Linked list is empty")  # check if the linked list is empty
        else:
            current = a
            while (current is not None):  # loop through each node
                length += 1  # increment length for each node
                print(current.value)  # print the value of the current node
                current = current.next  # move to the next node

    

if __name__ == "__main__":
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)
    a.next.next.next.next = Node(5)
    a.next.next.next.next.next = Node(6)

    b = reverse_k_group(a,3)

    printLL(b)
