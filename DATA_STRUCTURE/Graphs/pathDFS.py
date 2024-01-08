class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edge = edges
        self.adjacentMatrix = [[0 for i in range(vertices)] for j in range(vertices)]
        self.visited = [False for i in range(vertices)]

    def addEdge(self):
        for i in range(self.edge):
            a, b = [int(i) for i in input().split()]
            self.adjacentMatrix[a][b] = 1
            self.adjacentMatrix[b][a] = 1
        return
    
    def pathDFS(self, cv, v2):
        if cv == v2:
            return [v2]
        
        # if self.adjacentMatrix[cv][v2] == 1:
        #     return [v2, cv]
        self.visited[cv] = True
        for i in range(self.vertices):
            if self.adjacentMatrix[cv][i] == 1 and self.visited[i] == False:
                ans = self.pathDFS(i, v2)
                if ans is not None:
                    ans.append(cv)
                    return ans
        return None
    

v, e = [int(i) for i in input().split()]
g = Graph(v, e)
if v > 0:
    g.addEdge()
    v1, v2 = [int(i) for i in input().split()]
    if v1 < v and v2 < v:
        ans = g.pathDFS(v1, v2)

if ans is not None:
    for i in range(len(ans)):
        print(ans[i], end=" ")

