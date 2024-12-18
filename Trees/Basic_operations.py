# Node definition for a Binary Tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None  # Pointer to the right child
        self.left = None   # Pointer to the left child

# Tree definition
class Tree:
    def __init__(self, root=None):
        self.root = root  # Root node of the tree

    # Method to insert a new node into the tree
    def insert(self, data):
        new_node = TreeNode(data)  # Create a new node
        if self.root is None:  # If the tree is empty, set the new node as root
            self.root = new_node
        else:
            # Call helper method to recursively insert the node
            self.insert_recursively(self.root, new_node)
    
    # Helper method to insert a node into the correct position
    def insert_recursively(self, current, new_node):
        if current.data > new_node.data:  # Insert into the left subtree if data is smaller
            if current.left is None:
                current.left = new_node
            else:
                # Recur for the left subtree
                self.insert_recursively(current.left, new_node)
        else:  # Insert into the right subtree if data is larger or equal
            if current.right is None:
                current.right = new_node
            else:
                # Recur for the right subtree
                self.insert_recursively(current.right, new_node)

    # Method for inorder traversal (Left, Root, Right)
    def inorder(self, current):
        if current is None:  # Base case: if the current node is None, return
            return
        else:
            self.inorder(current.left)  # Traverse the left subtree
            print(current.data, end=" ")  # Visit the current node
            self.inorder(current.right)  # Traverse the right subtree
        return
    
    # Method for preorder traversal (Root, Left, Right)
    def preorder(self, current):
        if current is None:  # Base case: if the current node is None, return
            return
        else:
            print(current.data, end=" ")  # Visit the current node
            self.preorder(current.left)  # Traverse the left subtree
            self.preorder(current.right)  # Traverse the right subtree
        return
    
    # Method for postorder traversal (Left, Right, Root)
    def postorder(self, current):
        if current is None:  # Base case: if the current node is None, return
            return
        else:
            self.postorder(current.left)  # Traverse the left subtree
            self.postorder(current.right)  # Traverse the right subtree
            print(current.data, end=" ")  # Visit the current node
        return

# Create an instance of the Tree
ob1 = Tree()

# Insert nodes into the tree
ob1.insert(5)
ob1.insert(4)
ob1.insert(6)
ob1.insert(3)
ob1.insert(7)

# Perform inorder traversal and print the result
ob1.inorder(ob1.root)  # Expected: 3 4 5 6 7
print("\n")  # Add a newline for better formatting

# Perform preorder traversal and print the result
ob1.preorder(ob1.root)  # Expected: 5 4 3 6 7
print("\n")  # Add a newline for better formatting

# Perform postorder traversal and print the result
ob1.postorder(ob1.root)  # Expected: 3 4 7 6 5
