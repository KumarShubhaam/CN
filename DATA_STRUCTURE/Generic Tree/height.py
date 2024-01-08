import sys
class Tree():
    def __init__(self, data):
        self.data = data
        self.children = list()

#main
sys.setrecursionlimit(10**6)
## Read input as specified in the question.
## Print output as specified in the question.
def height(root):
    pass


def treeinput(arr):
    
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


def printTree(root):
    if root is None:
        return
    
    print(root.data, ": ", end="")
    for child in root.children:
        print(child.data,",", end=" ")
    print()  








# main
arr = [int(x) for x in input().split()]
print(arr)
root = treeinput(arr)
printTree(root)
# print(height())
