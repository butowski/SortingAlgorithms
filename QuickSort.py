from SortingAlgorithm import SortingAlgorithm

class QuickSort(SortingAlgorithm):

    def divide(self, left, right):
        """
        |  left  |    right   |
        |________|bound|______|
        We define that the bound is part of the right list. 
        Therefore, the bound will never be swapped and the bound index stays the same. 

        @return:

        |  left  |    right   |
        |________|bound|______|
                    |
        returns the index of the bound element. 
        """

        bound_idx = right
        bound = self.data[bound_idx]
    
        
        l = left
        r = right
        # while the pointers have not overtaken each other
        while l < r:
            #print("self.data[l]={}, pivot={}, self.data[r]={}".format(self.data[l], bound, self.data[r]))

            while self.data[l] <= bound and l < right: 
                # element is already on correct side
                l = l+1
                assert(l <= right)
            while self.data[r] >= bound and r > 0: 
                # element is already on correct side
                assert(r >= 0)
                r = r-1

            #print("self.data[l]={}, pivot={}, self.data[r]={}".format(self.data[l], bound, self.data[r]))
            if l < r: # check that pointers have not overtaken yet
                # swap two elements
                tmp = self.data[l]
                self.data[l] = self.data[r]
                self.data[r] = tmp
                
                # do not just advance pointers here after the swap. 
                # The pointers may only advanced if the invariants still hold. 
                # So continue with the while loop.


            
            #print(self.data)
        # The pointers have overtaken each other.
        # ensure that at least one element is in the correct position. Use method described by Hoare.
        # swap the bound with the element at the position pointed to by the l pointer. 
        tmp = self.data[l]
        self.data[l] = self.data[bound_idx]
        self.data[bound_idx] = tmp

        # finally return the index of the bound. 
        return l



    def quick_sort(self, left, right):
        # abort the recursion if the segment has only one or zero elements.
        if left < right: 
            bound_idx = self.divide(left, right)
            # We no have a left and a right segment
            #
            # |  left  |    right   |
            # |________|bound|______|
            # reduce the size of the right segment by one. (Exclude the bound element)
            # perform the quick sort again on the left and the new right segment
            
            self.quick_sort(left, bound_idx - 1)
            self.quick_sort(bound_idx + 1, right)

    def sort(self):
        self.quick_sort(0, len(self.data) - 1)



if __name__ == "__main__":
    #data = [5, 15, 20, 13, 7, 1, 0, 17, 17, 8, 18, 9, 5, 13, 1, 5, 7, 2, 16]

    #data = [7, 2, 4, 8, 3, 6]
    #data = [1,3,2]
    data = [46, 99, 8, 64, 71]
    # test the divide function
    #divided, _, pivot = divide(data)
    #print("divided with pivot {}\n{}".format(pivot, divided))

    # quick sort
    #quick_sort(data, 0, len(data)-1)
    #print("Sorted:\n{}".format(data))
    