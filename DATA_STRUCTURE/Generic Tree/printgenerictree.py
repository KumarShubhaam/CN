import sys 
from sys import stdin
class treeNode():
    def __init__(self, data):
        self.data = data
        self.children = list()

#main
sys.setrecursionlimit(10**6)
## Read input as specified in the question.
## Print output as specified in the question.
def height(root):
    pass


def treeinput():
    arr = list(int(x) for x in stdin.readline().rstrip().rsplit())
    queue = []
    rootdata = arr.pop(0)
    if rootdata == 0:
        return None
    root = Tree(rootdata)
    smallroot = root
    while len(arr) != 0:
        
        d = arr.pop(0)
        for i in range(d):
            child = Tree(arr.pop(0))
            queue.append(child)
            smallroot.children.append(child)
        if d != 0:
            smallroot = queue.pop(0)
    return root



def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root











def printTree(root):
    if root is None:
        return
    
    print(root.data, ": ", end="")
    for child in root.children:
        print(child.data,",", end=" ")
    print()  
    for c in root.children:
        printTree(c)








# main
arr = list(int(x) for x in stdin.readline().rstrip().rsplit())
root = createLevelWiseTree(arr)
printTree(root)
# print(height())
