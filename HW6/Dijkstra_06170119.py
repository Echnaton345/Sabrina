
# coding: utf-8

# In[2]:


import sys
from collections import defaultdict 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w])
  
    def printSolution1(self, dist): 
        print("Dijkstra{",end = '')
        for node in range(self.V): 
            print ("\'",node,"\'",":",dist[node],',',end = "")
        print("\b","}")
  
    def minDistance(self, dist, shortestArry): 
  
        min = float("inf") 
        for v in range(self.V): 
            if dist[v] < min and shortestArry[v] == False: 
                min = dist[v] 
                min_index = v 
        return min_index 

    def Dijkstra(self, s): 
  
        dist = [float("inf")] * self.V
        dist[s] = 0
        shortestArry = [False] * self.V 
        for cout in range(self.V): 
            u = self.minDistance(dist, shortestArry) 
            shortestArry[u] = True
            
            for v in range(self.V): 
                if self.graph[u][v] > 0 and shortestArry[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                    dist[v] = dist[u] + self.graph[u][v] 

        result = {}
        for i in range(self.V):
            result[str(i)] = dist[i]

        return result
     
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1

    def Kruskal(self): 
        result =[]  
        i = 0 
        e = 0 
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
        parent = [] ; rank = [] 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
        while e < self.V -1 : 
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
 
        output = {}
        for u, v, w in result:
            output[str(u)+'-'+str(v)]  = w 
        return output
        

