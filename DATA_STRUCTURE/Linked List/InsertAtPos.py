class node:
    def __init__(self, data):
            self.data = data
            self.next = None

def inputLL():
    n = [int(x) for x in input().split()]
    head = None
    i = 0
    while i < len(n) and n[i] != -1:
        newnode = node(n[i])

        if head is None:
            head = newnode
            tail = newnode
        else:
            tail.next = newnode
            tail = newnode
        i += 1
    return head

def printLL(head):
    curr = head
    while curr.next is not None:
        print( curr.data, '->', end='')
        curr = curr.next
    print(curr.data, '->', end='')
    print(None)

def insertnode(head, data, i):
    prev = None
    curr = head
    j = 1
    while curr.next is not None:
        j = j + 1
        curr = curr.next
    # print('j is', j)
    if i >= 0 and i <= j:
        newnode = node(data)
        curr = head
        
        for j in range(1, i):
            # print(curr.data)
            prev = curr
            curr = curr.next
        if prev is None:
            head = newnode
            newnode.next = curr
            return head
        else:
            prev.next = newnode
            newnode.next = curr
            return head
        
    else:
        print('i is out of range')
    
def deletenode(head, pos):
    prev = None
    curr = head
    j = 0
    while j < pos:
        prev = curr
        curr = curr.next
        j = j + 1
    prev.next = curr.next

def lengthRecursive(head):
    # A linked list, find and return the length of input LL recursively.
    # Write your code here
    count = 0
    if head.next is None:
        count = count + 1
        return count 
    
    count = lengthRecursive(head.next)
    count = count + 1
    # print(head.data, '->', count)
    return count

def findNode(head, n) :
    # Write your code here.
    count = -1
    print('here', head.data)
    if head.next is None:
        return -1
    
    if head.data == n:
        count = count + 1
        return count
    else:
        print(head.data)
        count = findNode(head.next, n)
    count = count + 1
    return count

def length(head):
    length = 0
    while head.next is not None:
        length += 1
        head = head.next
    
    return length+1

def reverse(head):
    if head is None or head.next is None:
        return head
    
    smallhead = reverse(head.next) 
    tail = head.next
    tail.next = head
    head.next = None
    return smallhead
   


head = inputLL()
# print('before inserting LL')
printLL(head)
# head = insertnode(head, 7, 3)
# print('after inserting LL')
# printLL(head)
# deletenode(head, 2)
# print('after deletiion')
# printLL(head)
# ans = lengthRecursive(head)
# print(ans)
# print(findNode(head, 5))
print(length(head))
head = reverse(head)
printLL(head)
