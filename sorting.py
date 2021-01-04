import numpy as np


class sorting:
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
        print("Sıralanmış:",self.array)


randomIntNumbers = np.random.randint(0,100,6)
print("Sıralanmamış:",randomIntNumbers)
sirala = sorting(randomIntNumbers)
sirala.selectionSort()