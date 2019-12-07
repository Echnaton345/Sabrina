
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
        x = int(h.hexdigest(), 16)
        index = x % self.capacity

        if self.data[index] == None:
            self.data[index] = ListNode(x)

        else:
            cn = self.data[index]
            if cn:
                while cn.next:
                    if cn.next.val == x:
                        return
                    else:
                        cn = cn.next

                cn.next = ListNode(x)

    def remove(self, key):
        h = MD5.new()
        h.update(key.encode(encoding='utf-8'))
        x = h.hexdigest
        x = int(h.hexdigest(), 16)
        index = x % self.capacity
        cn = self.data[index]
        pre = None
        while cn is not None:
            if cn.val == x:
                if pre is None:
                    self.data[index] = cn.next

                else:
                    pre.next = cn.next
                break
            else:
                pre = cn
                cur = cn.next

    def contains(self, key):
        h = MD5.new()
        h.update(key.encode(encoding='utf-8'))
        x = h.hexdigest
        x = int(h.hexdigest(), 16)
        index = x % self.capacity
        cn = self.data[index]
        while cn is not None:
            if cn.val == x:
                return True
            cn = cn.next

        return False

