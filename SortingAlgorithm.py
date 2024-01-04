class SortingAlgorithm:

    def __init__(self, data):
        self.data = data

    def sort(self):
        if self.data is None or len(self.data) <= 0:
            print("data is empty")
            return
        pass

    def is_sorted(self) -> bool:
        for i in range(0,len(self.data) - 1):
            self.assertTrue(self.data[i] <= self.data[i+1])
