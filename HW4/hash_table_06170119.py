
# coding: utf-8

# In[2]:


from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity

        
    def add(self, key):

        h = MD5.new()
        h.update(key.encode(encoding='utf-8'))
        x = h.hexdigest
        x = int(h.hexdigest(),16)
        index = x%self.capacity
        
        if self.data[index] == None:
            self.data[index] = ListNode(key)
        else:
            if self.data[index] != None:
                while self.data[index].val != key and self.data[index].next:
                    self.data[index] = self.data[index].next
                if self.data[index].val != key:
                    self.data[index].next = ListNode(key)
    
    def remove(self, key):

        h = MD5.new()
        h.update(key.encode(encoding='utf-8'))
        x = h.hexdigest
        x = int(h.hexdigest(),16)
        index = x%self.capacity
                       
        if self.data[index] and self.data[index].val == key:
            self.data[index] = self.data[index].next
            return
        pre = None
        while self.data[index]:
            if self.data[index].val == key:
                pre.next = self.data[index].next
                return
            pre = self.data[index]
            self.data[index] = self.data[index].next
        
    def contains(self, key):
        
        h = MD5.new()
        h.update(key.encode(encoding='utf-8'))
        x = h.hexdigest
        x = int(h.hexdigest(),16)
        index = x%self.capacity
       
        if self.data[index] ==None:
            return False
        
        n=self.data[index]
        if self.data[index].val == key:
            return True
        else:
            self.data[index]=self.data[index].next
            while self.data[index] !=None:
                if self.data[index].val == key:
                    return True
                else:
                    self.data[index]=self.data[index].next
            return False

