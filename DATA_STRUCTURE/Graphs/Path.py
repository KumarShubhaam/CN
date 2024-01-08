# Write your code here
class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacentMatrix = [[0 for i in range(vertices)] for j in range(vertices)]
        self.visited = [False for i in range(vertices)]

    def addEdge(self):
        for i in range(self.edges):
            a, b = [int(i) for i in input().split()]
            self.adjacentMatrix[a][b] = 1
            self.adjacentMatrix[b][a] = 1
        return
    
    # def pathHelper(self, cv, v2):
    #     if self.adjacentMatrix[cv][v2] == 1 :
    #         return True
    #     self.visited[cv] = True
    #     for i in range(self.vertices):
    #         if self.adjacentMatrix[cv][i] == 1 and self.visited[i] == False:
    #             ans = self.pathHelper(i, v2)
    #             if ans is True:
    #                 return True
    #     return False

        
    def path(self, cv, v2):
        # ans = self.pathHelper(v1, v2)
        # return ans
        if self.adjacentMatrix[cv][v2] == 1 :
            return True
        self.visited[cv] = True
        for i in range(self.vertices):
            if self.adjacentMatrix[cv][i] == 1 and self.visited[i] == False:
                ans = self.path(i, v2)
                if ans is True:
                    return True
        return False
        
        
        
v, e = [int(i) for i in input().split()]
g = Graph(v, e)  
if v > 0:
    g.addEdge()
    v1, v2 = [int(i) for i in input().split()]
    # print('the v1 is {} and the v2 is {}'.format(v1, v2))
    if v1 < v and v2 < v:
        ans = g.path(v1, v2)
    else:
        ans = False
if ans is True:
    print('true')
else:
    print('false') 