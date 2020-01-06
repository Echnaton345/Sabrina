
# coding: utf-8

# In[1]:


class MinStack:

    def __init__(self):
        self.s=[]

    def push(self, x: int) -> None:
        self.s.append(x)
        

    def pop(self) -> None:
        self.s.pop()
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return min(self.s)

