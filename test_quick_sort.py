import unittest
import QuickSort
import random
import numpy as np

class TestQuickSort(unittest.TestCase):
    def is_sorted(self, data) -> bool:
        for i in range(0,len(data) - 1):
            self.assertTrue(data[i] <= data[i+1])

    def get_random_list(self, length):
        return [random.randint(0,100) for _ in range(0,length)]

    def test_quick_sort(self):
        candidates = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
        ]
        #for c in candidates:
        for c in candidates:
            print("Testing {}".format(c))
            QuickSort.quick_sort(c, 0, len(c) - 1)
            print("Sorted: {}".format(c))
            self.is_sorted(list(c))

    def test_quick_sort_random(self):
        candidates = [self.get_random_list(10) for x in range(0,10)]
        print(candidates)
        for c in candidates:
            print("Testing {}".format(c))
            QuickSort.quick_sort(c, 0, len(c) - 1)
            print("Sorted: {}".format(c))
            self.is_sorted(list(c))


    def test_np_array(self):
        arr = np.array([3,2,1,5,5,1,3])
        QuickSort.quick_sort(arr, 0, len(arr)-1)
        print(arr)

if __name__ == '__main__':
    unittest.main()
