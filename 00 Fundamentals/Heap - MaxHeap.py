# Source code source: by Joe James https://www.youtube.com/watch?v=GnKHVXv_rlQ&ab_channel=JoeJames

class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]     # creating an empty list. 0 is index

        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1)
    
    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)
    
    def peek(self):
        if self.heap[1]:            # check if the list is not empty. If there is at least a value, return the max.
            return self.heap[1]     
        else:
            return False            # if not, return false.
    
    # 3 possibilities for pop function
    # 1) there are 2 or more values in the heap. swap the max value to the end of the heap and pop if off.
    # 2) there is only 1 value - pop it off and return an empty heap.
    # 3) try to pop off an empty heap, so return False in this case. 

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1) # swap the first and last value. 
            max = self.heap.pop()              # then pop off the last. 
            self.__bubbleDown(1)               # then bubble down the value in position 1 to its proper position. 
        
        elif len(self.heap) == 2:              # if there are only 2 values in the heap
            max = self.heap.pop()              # pop off the last one and store it in max. 
        
        else:
            max = False
        return max

    
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    # 2 possibilities for floatUp:
    # 1) the index passed in is 1, so there is no floating to be done. 
    def __floatUp(self, index):     # it's recursive, until it hits its best case.   
        parent = index // 2         # first, let's start by finding the parent index to float our value up.
        if index <= 1:              # if index is 1 (there's only one item), do nothing.
            return
        
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)
    
    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)
