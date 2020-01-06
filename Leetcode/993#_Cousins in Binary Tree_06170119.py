
# coding: utf-8

# In[1]:


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
     def isCousins(self, root, x, y):
      
        def f(root, v, p):
            if root.val == v:
                _d = 1
                _p = p
                return _d, _p
            
            if root.left!=None:
                l_d, l_p = f(root.left, v, root.val)
                if l_d!=None:
                    return l_d+1, l_p
                
            if root.right!=None:
                r_d, r_p = f(root.right, v, root.val)
                if r_d!=None:
                    return r_d+1, r_p             
            return None, p
			
        _x = f(root, x, None)
        _y = f(root, y, None)
        return (_x[0] == _y[0]) and (_x[1] != _y[1])

