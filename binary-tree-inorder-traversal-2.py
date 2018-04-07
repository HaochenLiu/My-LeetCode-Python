# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iteratively   
class Solution:
    def inorderTraversal(self, root):
        res = []
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
                
            if not stack:
                return res
            
            node = stack.pop()
            res.append(node.val)
            root = node.right
