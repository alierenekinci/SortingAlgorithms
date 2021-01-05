import numpy as np


class array:
    def __init__(self,liste):
        if(type(liste) == list): 
            self.array = np.array(liste)
            self.arraySize = self.array.size
        elif(type(liste) == np.ndarray):
            self.array = liste
            self.arraySize = liste.size
        else:
            print("Liste halinde vermek zorundasın.")
    
    def selectionSort(self):
        for i in range(self.arraySize - 1):
            for j in range(i + 1, self.arraySize):
                if(self.array[j] < self.array[i]):
                    self.array[j], self.array[i] = self.array[i] , self.array[j]
        return self.array        

    def bubbleSort(self):
        for i in range(self.arraySize):
            for j in range(self.arraySize-1):
                if self.array[j + 1] < self.array[j]:
                    self.array[j + 1], self.array[j] = self.array[j] , self.array[j + 1]
                    i *= 1
        return self.array 
    
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
                return self.array
        
                
                
            




"""
randomIntNumbers = np.random.randint(0,100,6)
print("Sıralanmamış:",randomIntNumbers)
sirala = sorting(randomIntNumbers)
sirala.selectionSort()
"""