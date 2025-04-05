#Pre order traversal of tree using recursion


class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = []

    def preorderTraversal(self,root):
        if not root:
            return self.ans
        self.ans.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.ans
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
    
ob = Solution()
print(ob.preorderTraversal(root))

