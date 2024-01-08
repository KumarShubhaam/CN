# Write your code here
import queue
class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.adjacentMatrix = [[0 for i in range(vertices)] for j in range(vertices)]
        self.visited = dict.fromkeys([int(i) for i in range(vertices)], False)
        self.edges = edges
    
    def addEdge(self):
        for i in range(self.edges):
            a, b = [int(i) for i in input().split()]
            self.adjacentMatrix[a][b] = 1
            self.adjacentMatrix[b][a] = 1
        return

    def BFS(self):
        q = queue.Queue()
        # sv = 0
        
        for sv in range(self.vertices):
            if self.visited[sv] == False:
                q.put(sv)
                self.visited[sv] = True
                while q.empty() is False:
                    sv = q.get()
                    # if self.visited[sv] == False:
                    print(sv, end=" ")
                    for i in range(self.vertices):
                        if self.adjacentMatrix[sv][i] == 1 and self.visited[i] == False:
                            q.put(i)   
                            self.visited[i] = True 
        return
    
    def BFS2Helper(self, q):
        if q.empty() is True:
            return
        sv = q.get() 
        print(sv, end=" ")
        self.visited[sv] = True
        for i in range(self.vertices):
            if self.adjacentMatrix[sv][i] == 1 and self.visited[i] == False:
                q.put(i)
                self.visited[i] = True
                
        # nv = q.get()  
        self.BFS2Helper(q)
        return

    def BFS2(self):
        q = queue.Queue()
        q.put(0)  
        self.BFS2Helper(q)
        for sv in range(self.vertices):
            if self.visited[sv] == False:
                q.put(sv)  
                self.BFS2Helper(q)
        return


V, E = [int(i) for i in input().split()]
g = Graph(V, E)
g.addEdge()
if V > 0:
    g.BFS()
    # g.BFS2()
