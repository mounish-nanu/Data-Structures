# Definition for a tree node
class TreeNode:
    def __init__(self, data):
        self.data = data  # Store data in the node
        self.right = None  # Pointer to the right child node
        self.left = None   # Pointer to the left child node

# Tree definition
class Tree:
    def __init__(self, root=None):
        self.root = root  # Initialize the tree with an optional root node

    # Method to insert a new node into the tree
    def insert(self, data):
        new_node = TreeNode(data)  # Create a new node with the given data
        if self.root is None:  # If the tree is empty, set the new node as the root
            self.root = new_node
        else:
            # Call the helper method to recursively insert the node
            self.insert_recursively(self.root, new_node)
    
    # Helper method to insert a node into the correct position in the tree
    def insert_recursively(self, current, new_node):
        # Check if the new node's data is smaller than the current node's data
        if current.data > new_node.data:
            if current.left is None:  # If the left child is None, insert here
                current.left = new_node
            else:
                # Recur for the left subtree
                self.insert_recursively(current.left, new_node)
        else:  # Otherwise, insert into the right subtree
            if current.right is None:  # If the right child is None, insert here
                current.right = new_node
            else:
                # Recur for the right subtree
                self.insert_recursively(current.right, new_node)

    # Method to calculate the height of the tree starting from a given node
    def height(self, current):
        if current is None:  # Base case: if the node is None, return -1
            return -1
        else:
            # Recursively calculate the height of the left and right subtrees
            # Add 1 to the maximum of the heights to include the current node
            return 1 + max(self.height(current.left), self.height(current.right))


# Create an instance of the Tree
ob1 = Tree()

# Insert nodes into the tree
ob1.insert(5)  # Insert 5 as the root node
ob1.insert(4)  # Insert 4 into the tree
ob1.insert(6)  # Insert 6 into the tree
ob1.insert(3)  # Insert 3 into the tree
ob1.insert(7)  # Insert 7 into the tree

# Print the height of the tree
# The height is calculated from the root node to the deepest leaf node
print(ob1.height(ob1.root))
