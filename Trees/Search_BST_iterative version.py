#This function implements search operation on binary tree in a iterative way
# If a node with value is found, it will return the nodes address, 
# if you need to see the value of the node, just change that return t to return t.val in while loop

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        t = root

        while t is not None :
            if t.val == val:
                return t
            elif t.val > val:
                t = t.left
            else:
                t = t.right
        return None
    
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

val = 2

ob1 = Solution()
print(ob1.searchBST(root,val))