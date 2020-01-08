
# coding: utf-8

# In[1]:


def partition(arr,low,high):  #partition() 方法用來根據指定的分隔符將字符串進行分割。
    i = ( low-1 )         # index of smaller element，將位置往左邊，把i設成最左邊-1
    pivot = arr[high]     # pivot，選一個中心點，右邊的
  
    for j in range(low , high): #for 與 in 連用， in 後面接多個元素的物件。
  
        if   arr[j] < pivot: # If current element is smaller than the pivot 
          
            # increment index of smaller element 
            i = i+1 #原本左邊的要+1
            arr[i],arr[j] = arr[j],arr[i] #把i與j得值交換
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
def quickSort(arr,low,high):
    if low < high: 
  
        pi = partition(arr,low,high)
  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
arr = [10, 7, 8, 9, 1, 5]  #Test
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),

