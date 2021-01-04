import numpy as np


class sorting:
    def __init__(self,liste):
        if(type(liste) == list): 
            self.array = np.array(liste)
            self.arraySize = self.array.size
        else:
            print("Liste halinde vermek zorundasın.")
    
    def selectionSort(self):
        pass

sirala = sorting([1,2,36,7])
sirala.selectionSort()