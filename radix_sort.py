from SortingAlgorithm import SortingAlgorithm

class RadixSort(SortingAlgorithm):


    def __init__(self, data, max_num_digits):
        super().__init__(data)
        self.max_num_digits = max_num_digits
        print("max num digits {}".format(self.max_num_digits))


    def get_digit(self, value, place) -> int:
        if place == 0:
            return value % 10
        elif place >0:
            return (value // (pow(10,place))) % 10

    def partition(self, arr, place):
        buckets = {str(key): [] for key in range(0,10)}
        # partition into 10 bucket. (0-9)
        proceed = False
        for i in range(0,len(arr)):
            key = self.get_digit(arr[i], place)
            if key !=0: # TODO: this fails for [400,200,100]
                proceed = True
            buckets[str(key)].append(arr[i])
        if proceed == False:
            return None
        return buckets
    

    



    def collect(self, buckets):
        data = []
        for i in range(0, 10):
            for item in buckets[str(i)]:
                data.append(item)

        return data

    def sort(self):
        for i in range(self.max_num_digits):
            buckets = self.partition(self.data, i)
            if buckets is None:
                break
            self.data = self.collect(buckets)

class RadixSortEfficient(RadixSort):

    def partition(self, arr, place):
        """
        An implementation of the partitioning using two lists (instead of a dict with lists for each bucket. )

        """
        # Fist pass over the data. Determine how many items per key there are. 
        count = [0] * 11
        # count
        # |0|count for key 0 | count key 1| ... | count key 9 |
        # the leading zero is neeed in the second pass so that count[key=0] gives address 0.

        for i in range(0,len(arr)):
            key = self.get_digit(arr[i], place)
            count[key+1] += 1
        # adjust count to point to the corresponding address in the data
        for i in range(1, len(count)):
            count[i] += count[i-1]  
    
        # Second pass over the data.
        data_new = [0] * len(arr)
        for i in range(0, len(arr)):
            key = self.get_digit(arr[i], place)
            assert(data_new[count[key]]==0)
            data_new[count[key]] = arr[i]
            count[key] += 1

        # return the new list
        return data_new
    
    def sort(self):
        for i in range(self.max_num_digits):
            self.data = self.partition(self.data, i)
