# https://www.physics.drexel.edu/~valliere/PHYS405/sort_algorithms/sort_algorithm.html
import math
from SortingAlgorithm import SortingAlgorithm

class BubbleSort(SortingAlgorithm):

    def sort(self):
        SortingAlgorithm.sort(self)  # call base method

        for j in range(0, len(self.data) - 1):
            for i in range(0, len(self.data) -j-1):
                if self.data[i] > self.data [i+1]:
                    # swap
                    tmp = self.data[i]
                    self.data[i] = self.data[i+1]
                    self.data[i+1] = tmp
                #print(self.data)
        
    
        


