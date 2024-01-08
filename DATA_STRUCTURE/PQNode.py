class PqNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def isEmpty(self):
        #Implement the isEmpty() function here
        if self.getSize() == 0:
            return True
        else:
            return False
    
    def getSize(self):
        #Implement the getSize() function here
        return len(self.pq)

    def getMax(self):
        #Implement the getMax() function here
        return self.pq[0].value
    
    def printQueue(self):
        print('list', end= " ")
        for i in range(self.getSize() - 1):
            print(self.pq[i].value, end= " ")
        print()  
            

    def __percolateUp(self):
        childIndex = self.getSize() -1 
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            # self.printQueue()
            if self.pq[parentIndex].priority < self.pq[childIndex].priority:
                self.pq[parentIndex], self.pq[childIndex] = self.pq[childIndex], self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self,ele,priority):
        #Implement the insert() function here
        node = PqNode(ele, priority)
        self.pq.append(node)
        self.__percolateUp()
                
    def __percolateDown(self):
        parentIndex = 0
        leftChildIndex = 2*parentIndex + 1
        rightChildIndex = 2*parentIndex + 2
        while leftChildIndex < self.getSize()  :
            leftChildIndex = 2*parentIndex + 1
            rightChildIndex = 2*parentIndex + 2
            maxIndex = parentIndex
            if leftChildIndex < self.getSize() and  self.pq[leftChildIndex].priority > self.pq[maxIndex].priority:
                maxIndex = leftChildIndex
            elif rightChildIndex < self.getSize() and  self.pq[rightChildIndex].priority > self.pq[maxIndex].priority:
                maxIndex = rightChildIndex
            
            if maxIndex == parentIndex:
                break
            self.pq[maxIndex] , self.pq[parentIndex] = self.pq[parentIndex], self.pq[maxIndex]
            parentIndex = maxIndex

        
    
    def removeMax(self):
        #Implement the removeMax() function here
        if self.getSize() == 0:
            return None
        ans = self.pq[0].value
        self.pq[0] = self.pq[self.getSize() - 1] 
        self.pq.pop() 
        self.__percolateDown()
        return ans
        
myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1