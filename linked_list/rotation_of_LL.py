class Node:
    # Node class to represent each element in the linked list
    def __init__(self, value):
        self.value = value  # The value of the node
        self.next = None    # Pointer to the next node, initially set to None

class LinkedList:
    # LinkedList class to handle all operations for the linked list
    def __init__(self):
        self.head = None  # Initially, the linked list is empty, so head is None

    def insert_at_start(self, value):
        # Function to insert a new node at the start of the linked list
        newNode = Node(value)  # Create a new node with the given value
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = newNode
        else:
            # Otherwise, set the new node's next pointer to the current head
            # and then update the head to the new node
            newNode.next = self.head
            self.head = newNode
        return

    def insertAtIndex(self, index, value):
        # Function to insert a new node at a specific index in the linked list
        newNode = Node(value)  # Create a new node with the given value
        if index == 0:
            # If index is 0, simply insert the node at the start
            self.insert_at_start(value)
            return

        current = self.head  # Start at the head of the list
        k = 0  # Initialize counter to track the current index
        # Traverse the list to find the node just before the specified index
        while current is not None and k + 1 != index:
            current = current.next  # Move to the next node
            k = k + 1  # Increment index counter
        # If we found a valid node at the given index, insert the new node
        if current is not None:
            newNode.next = current.next  # Set the new node's next pointer to current node's next
            current.next = newNode  # Update the current node's next pointer to the new node
    
    def printLL(self):
        # Function to print all values in the linked list
        self.length = 0  # Initialize length counter to track the number of nodes
        if self.head is None:
            # If the list is empty, print an empty message
            print("Linked list is empty")
        else:
            current = self.head  # Start from the head of the list
            # Loop through each node until the end of the list
            while current is not None:
                self.length += 1  # Increment length counter for each node
                print(current.value)  # Print the value of the current node
                current = current.next  # Move to the next node
        return
    
    def rotate(self, k):
        # Function to rotate the linked list by k positions
        newNode = Node("trial")  # Temporary node to assist with rotation
        temp = newNode  # Keep a reference to the temporary node
        i = 0  # Counter for tracking the number of rotations
        # Perform k rotations
        while i < k:
            current = self.head  # Start from the head of the list
            self.head = current.next  # Move the head to the next node
            newNode.next = current  # Link the new node's next to the current node
            newNode = current  # Update newNode to point to the current node
            i = i + 1  # Increment the rotation counter
        
        newNode.next = None  # Set the new last node's next to None (end of list)
        point = self.head  # Start from the new head
        # Traverse to the last node of the list
        while point.next is not None:
            point = point.next
        point.next = temp.next  # Link the last node to the rotated portion
        temp.next = None  # Ensure temporary node is not linked to any node
        return

# Driver code
LL = LinkedList()  # Create a new linked list instance
LL.insertAtIndex(0, 5)  # Insert 5 at index 0
LL.insertAtIndex(1, 6)  # Insert 6 at index 1
LL.insertAtIndex(2, 7)  # Insert 7 at index 2
LL.insertAtIndex(3, 30)  # Insert 30 at index 3
LL.insertAtIndex(4, 31)  # Insert 31 at index 4
LL.insertAtIndex(5, 32)  # Insert 32 at index 5
LL.rotate(4)  # Rotate the list by 4 positions
LL.printLL()  # Print the rotated linked list
