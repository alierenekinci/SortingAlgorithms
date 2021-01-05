import numpy as np


class array:
    def __init__(self,arr, fromSmallToLarge= True):
        self.fromSmallToLarge = fromSmallToLarge
        if(type(arr) == list): 
            self.array = np.array(arr)
            self.arraySize = self.array.size
        elif(type(arr) == np.ndarray):
            self.array = arr
            self.arraySize = arr.size
        else:
            print("Liste halinde vermek zorundasın.")
    
    def axisConvert(self):
        if self.fromSmallToLarge == True:
            return self.array
        else:
            temp = list()
            for i in range(self.arraySize-1,0, -1):
                temp.append(self.array[i])
            self.array = temp
            return self.array

    
    def selectionSort(self):
        for i in range(self.arraySize - 1):
            for j in range(i + 1, self.arraySize):
                if(self.array[j] < self.array[i]):
                    self.array[j], self.array[i] = self.array[i] , self.array[j]
        return self.axisConvert()        

    def bubbleSort(self):
        for i in range(self.arraySize):
            for j in range(self.arraySize-1):
                if self.array[j + 1] < self.array[j]:
                    self.array[j + 1], self.array[j] = self.array[j] , self.array[j + 1]
                    i *= 1
        return self.axisConvert()  
    
    def cocktailSort(self):
        for i in range(self.arraySize-1, 0, -1):
            isSwapped = False

            for j in range(i, 0, -1):
                if self.array[j] < self.array[j-1]:
                    self.array[j], self.array[j-1] = self.array[j-1] , self.array[j]
                    isSwapped = True
            
            for j in range(i):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j+1] = self.array[j+1] , self.array[j]
                    isSwapped = True
            
            if not isSwapped:
                return self.axisConvert()
        
                
                
            




"""
randomIntNumbers = np.random.randint(0,100,6)
print("Sıralanmamış:",randomIntNumbers)
sirala = sorting(randomIntNumbers)
sirala.selectionSort()
"""