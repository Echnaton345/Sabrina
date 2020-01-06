
# coding: utf-8

# In[ ]:


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def rec(root, val):
            if not root: return True
            if root.val == val:
                return rec(root.left,val) and rec(root.right,val)
            else:
                return False
        return rec(root, root.val)
        

