
# coding: utf-8

# In[ ]:


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if root == None:
            root = TreeNode(val)
            return root
        else:
            return self._insert(val, root)

    def _insert(self, val, now_node):
        
        if val <= now_node.val:
            if now_node.left is None:
                now_node.left = TreeNode(val)
                return now_node.left;
            else:
                return self._insert(val, now_node.left)

        elif val > now_node.val:
            if now_node.right is None:
                now_node.right = TreeNode(val)
                return now_node.right;
            else:
                return self._insert(val, now_node.right)

    def count(self, root, target):
        count=0
        nextnode = root
        while nextnode != None:
            nextnode = self.search(nextnode,target)
            if nextnode != None:
                nextnode = nextnode.left
                count = count +1
        return count

    def search(self, root, target):
        if root == None or target == root.val:
            return root

        elif target < root.val:
            return self.search(root.left,target)
      
        elif target > root.val:
            return self.search(root.right,target)

    def modify(self,root,target,new_val):
        count = self.count(root,target)
        self.delete(root,target)
        for i in range(0,count):
            self.insert(root,new_val)  
    
    def delete(self, root, target):
        if root == None:
            return root

        elif root.val > target:
            root.left = self.delete(root.left,target)

        elif root.val < target:
            root.right = self.delete(root.right,target)

        else: #root.val == target
      
            if root.left != None and root.right !=None:
                max_node,max_parent,max_depth = self.max(root.left)
                min_node,min_parent,min_depth = self.min(root.right)

                if max_depth >= min_depth:
                    root.val = max_node.val
                    root.left = self.delete(root.left,max_node.val);
          
                else:
                    root.val = min_node.val
                    root.right = self.delete(root.right,min_node.val);

            elif root.left != None:
        #root.val = root.left.val
              root = self.delete(root.left,root.val)
            elif root.right != None:
        #root.val = root.right.val
              root = self.delete(root.right,root.val)
    
            else:
              root = None;

        return root

    def min(search,root):
        depth = 0
        parent = None;
        current = root;
        while current.left!=None:
            parent = current;
            current=current.left
            depth = depth +1
        return current,parent,depth;

    def max(search,root):
        depth = 0
        parent = None;
        current = root;
        while current.right!=None:
            parent = current;
            current=current.right
            depth = depth +1
        return current,parent,depth;

