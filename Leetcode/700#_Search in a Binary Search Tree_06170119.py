
# coding: utf-8

# In[1]:


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def searchBST(self, root, val):
        
        while root:
            if val > root.val:
                root = root.right
            elif val < root.val:
                root = root.left
            else:
                return root
        
        return None       

