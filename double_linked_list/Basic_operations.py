class Node:
    def __init__(self, data):
        # Initialize the node with data and pointers to the previous and next nodes.
        self.data = data
        self.previous = None
        self.next = None

class DLL:
    def __init__(self):
        # Initialize the doubly linked list with an empty head.
        self.head = None
    
    def insert_at_start(self, data):
        # Insert a new node with given data at the start of the doubly linked list.
        newNode = Node(data)
        
        # If the linked list is empty, the new node becomes the head.
        if self.head is None:
            self.head = newNode
        else:
            # If the list is not empty, link the new node to the head and adjust pointers.
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode  # Make the new node the head of the list.
    
    def insert_at_index(self, data, i):
        # Insert a new node with the given data at the specified index in the doubly linked list.
        
        if self.head is None:
            print("Linked list is empty")  # If the list is empty, print a message.
            return
        
        newNode = Node(data)  # Create a new node with the provided data.

        current = self.head
        k = 0
        # Traverse the list to find the node at the desired index.
        while current is not None and k < i:
            current = current.next
            k += 1
        
        # If the current node is None, it means the index is beyond the current list length.
        if current is None:
            # Insert the new node at the end of the list.
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode  # Link the last node to the new node.
            newNode.previous = current  # Set the new node's previous pointer to the last node.
        
        else:
            # Insert the new node in between two nodes.
            newNode.next = current  # New node's next points to the current node.
            newNode.previous = current.previous  # New node's previous points to the previous node.
            if current.previous is not None:
                current.previous.next = newNode  # Adjust the previous node's next pointer.
            current.previous = newNode  # Adjust the current node's previous pointer.

    def print_DLL(self):
        # Print the elements of the doubly linked list from the head to the tail.
        print("Printing list forwards:")
        
        if self.head is None:
            print("Linked list is empty")  # If the list is empty, print a message.
        else:
            current = self.head
            while current is not None:
                print(current.data)  # Print the data of the current node.
                current = current.next  # Move to the next node in the list.
    
    def print_DLL_from_last(self):
        # Print the elements of the doubly linked list from the tail to the head.
        print("Printing list backwards:")
        
        current = self.head
        # Traverse to the last node of the list.
        while current.next is not None:
            current = current.next
        
        # Print the list from the last node to the head.
        while current is not None:
            print(current.data)  # Print the data of the current node.
            current = current.previous  # Move to the previous node in the list.

# Create an instance of the doubly linked list (DLL).
ob = DLL()
# Insert nodes at specific positions.
ob.insert_at_start(3)  # Insert 3 at the start.
ob.insert_at_index(4, 1)  # Insert 4 at index 1.
ob.insert_at_index(5, 2)  # Insert 5 at index 2.
ob.insert_at_index(7, 3)  # Insert 7 at index 3.
ob.insert_at_index(6, 3)  # Insert 6 at index 3 (between 7 and 5).
# Print the list from head to tail.
ob.print_DLL()
# Print the list from tail to head.
ob.print_DLL_from_last()
