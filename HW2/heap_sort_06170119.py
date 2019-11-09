
# coding: utf-8

# In[2]:


class Solution(object):

    def heap_sort(self,nums):
        self.build_max_heap(nums)
        n = len(nums)
        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.max_heapify(nums, index=0, size=i)
        return nums
            
    def father(self,i):
        return i //2
    
    def left(self,i):
        return 2*i
    
    def right(self,i):
        return 2*i + 1
    
    def build_max_heap(self,nums):
        length = len(nums)
        start = self.father(length - 1)
        while start >= 0:
            self.max_heapify(nums, index=start, size=length)
            start = start - 1
            
    def max_heapify(self,nums,index,size):
        l = self.left(index)
        r = self.right(index)
        if (l < size and nums[l] > nums[index]):
            largest = l
        else:
            largest = index
        if (r < size and nums[r] > nums[largest]):
            largest = r
        if (largest != index):
            nums[largest],nums[index] = nums[index], nums[largest]
            self.max_heapify(nums, largest, size)
    

