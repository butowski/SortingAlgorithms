import unittest
import random
import numpy as np
from insertion_sort import InsertionSort
from BubbleSort import BubbleSort
from QuickSort import QuickSort

class TestAlgorithms(unittest.TestCase):
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
            qs = QuickSort(c)
            qs.sort()
            print("Sorted: {}".format(c))
            self.is_sorted(list(c))

    def test_quick_sort_random(self):
        candidates = [self.get_random_list(10) for x in range(0,10)]
        print(candidates)
        for c in candidates:
            print("Testing {}".format(c))
            qs = QuickSort(c)
            qs.sort()
            print("Sorted: {}".format(c))
            self.is_sorted(list(c))

    def test_insertion_sort(self):
        data = [3, 5, 6, 1, 4, 2, 8, 1]
        insertion_sort = InsertionSort(data)
        insertion_sort.sort()
        self.is_sorted(insertion_sort.data)

    def test_insertion_sort(self):
        candidates = [self.get_random_list(10) for x in range(0,10)]
        for c in candidates:
            insertion_sort = InsertionSort(c)
            insertion_sort.sort()
            self.is_sorted(insertion_sort.data)



    def test_np_array(self):
        arr = np.array([3,2,1,5,5,1,3])
        qs = QuickSort(arr)
        qs.sort()
        print(arr)

if __name__ == '__main__':
    unittest.main()
