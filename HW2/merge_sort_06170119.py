
# coding: utf-8

# In[1]:


class Solution(object):
    
    
    def merge_sort(self,nums):
        print("nums"+ str(nums))
        if len(nums) <= 1:
            return nums
    
        midpoint = int(len(nums) / 2)
        
        left = self.merge_sort(nums[:midpoint])
        right = self.merge_sort(nums[midpoint:])
        return self.merge(left, right)
    
    def merge(self,m_left, m_right):
        result = []
        left_pointer = right_pointer = 0
        while left_pointer < len(m_left) and right_pointer < len(m_right):
            if m_left[left_pointer] < m_right[right_pointer]:
                result.append(m_left[left_pointer])
                left_pointer += 1
            else:
                result.append(m_right[right_pointer])
                right_pointer += 1
   
        result.extend(m_left[left_pointer:])
        result.extend(m_right[right_pointer:])
        
        return result


