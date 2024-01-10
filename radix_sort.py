from SortingAlgorithm import SortingAlgorithm

class RadixSort(SortingAlgorithm):

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
            if key !=0:
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
        i = 0
        while True:
            buckets = self.partition(self.data, i)
            if buckets is None:
                break
            self.data = self.collect(buckets)
            i = i+1