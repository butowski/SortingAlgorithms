from SortingAlgorithm import SortingAlgorithm

class QuickSort(SortingAlgorithm):

    def __init__(self, data, **kwargs):
        super().__init__(data, **kwargs)
        self.use_optimization = kwargs.get('use_optimization', False)

    # ---------- optimization with insertion sort ------
    def shift_right(self, left, right):
        """
        Shifts the segment between left (inclusive) and right (exclusive) to the right by 1.
        """
        for i in range(right, left, -1):
            self.data[i] = self.data[i-1]

    # TODO: only perform insertion sort on a segment of the list
    def seg_insertion_sort(self, left, right):
        """
        Perform insertion sort on a segment of the list
        """
        i = left + 1  # the first element is trivially sorted
        while i < right + 1:
            for j in range(left, i):
                if self.data[i] < self.data[j]:
                    # found the position
                    tmp = self.data[i] 
                    # shift all values [0, i-1] to the right by 1
                    self.shift_right(j,i)
                    # insert the value
                    self.data[j] = tmp
                    break 
            i = i+1

    # ----------- end optimization code --------------

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
        returns the index of the bound element or -1 if the segment does not need rufther dividing. 
        """

        # optimization for small segments
        if self.use_optimization and right - left < 7:
            self.seg_insertion_sort(left, right)
            return -1 #  terminate the recursion

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

            # optimization: if the segment was sorted with insertion sort the bound_idx is -1
            # then we stop the recursion and return
            if not bound_idx == -1:
                # We now have a left and a right segment
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
    #data = [1,3,2,1]
    data = [46, 99, 8, 64, 71]
    
    # quick sort
    qs = QuickSort(data, use_optimization=True)
    qs.sort()
    
    #quick_sort(data, 0, len(data)-1)
    print("Sorted:\n{}".format(qs.data))
    