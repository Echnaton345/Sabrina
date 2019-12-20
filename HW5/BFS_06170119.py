
# coding: utf-8

# In[1]:


from collections import defaultdict  
class Graph:  
    def __init__(self):   
        self.graph = defaultdict(list)  
  
    def addEdge(self,u,v):  
        self.graph[u].append(v)  
 
    def BFS(self, s):
        queue = [s]
        visited = []
 
        while queue:
            node = queue.pop(0)
            if node in visited:
                continue
            else:
                visited.append(node)
                i = self.graph[node]
                for neighbour in i:
                    queue.append(neighbour)
        return visited
    
    def DFS(self, s):
        stack = [s]
        visited = []

        while stack:
            s = stack.pop(-1)
            if s in visited:
                continue
            else:
                visited.append(s)
                for neighbor in self.graph[s]:
                    stack.append(neighbor)
        return visited

