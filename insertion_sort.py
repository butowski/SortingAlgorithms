from SortingAlgorithm import SortingAlgorithm

class InsertionSort(SortingAlgorithm):

    def shift_right(self, left, right):
        """
        Shifts the segment between left (inclusive) and right (exclusive) to the right by 1.
        """
        for i in range(right, left, -1):
            self.data[i] = self.data[i-1]

    def sort(self):
        i = 1  # the first element is trivially sorted
        while i < len(self.data):
            for j in range(0, i):
                if self.data[i] < self.data[j]:
                    # found the position
                    tmp = self.data[i] 
                    # shift all values [0, i-1] to the right by 1
                    self.shift_right(j,i)
                    # insert the value
                    self.data[j] = tmp
                    break 
            i = i+1
                    


if __name__ == "__main__":
    data = [3,5,6,1,4,2,8,1,2,4,8,9,1,4,6]
    insert_sort = InsertionSort(data)
    print(insert_sort.data)
    #insert_sort.shift_right(0,3)
    insert_sort.sort()
    print(insert_sort.data)