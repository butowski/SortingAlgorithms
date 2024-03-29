from collections.abc import Sequence
import unittest
import random
import numpy as np
from insertion_sort import InsertionSort
from BubbleSort import BubbleSort
from QuickSort import QuickSort
from SortingAlgorithm import SortingAlgorithm
from merge_sort import MergeSort
from radix_sort import RadixSort, RadixSortEfficient

class TestAlgorithms(unittest.TestCase):
    def is_sorted(self, data) -> bool:
        for i in range(0,len(data) - 1):
            self.assertTrue(data[i] <= data[i+1])

    def get_random_list(self, length, num_range):
        return [random.randint(0,num_range) for _ in range(0,length)]

    def perform_random_test(self, alg, num_range=100, verbose=False, **kwargs):
        candidates = [self.get_random_list(10, num_range) for x in range(0,10)]
        for c in candidates:
            instance = alg(c, **kwargs)
            instance.sort()
            self.is_sorted(instance.data)
            print(instance.data)


    # ------------- individual test cases ------------------

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
        self.perform_random_test(QuickSort)
        
    def test_quick_sort_optimized(self):
        c = [2,1,4,3]
        qs_opt = QuickSort(c, use_optimization=True)
        qs_opt.sort()
        self.is_sorted(qs_opt.data)

    def test_quick_sort_optimized_random(self):
        self.perform_random_test(QuickSort, use_optimization=True)
        
    

    def test_insertion_sort(self):
        data = [3, 5, 6, 1, 4, 2, 8, 1]
        insertion_sort = InsertionSort(data)
        insertion_sort.sort()
        self.is_sorted(insertion_sort.data)

    def test_insertion_sort(self):
        self.perform_random_test(InsertionSort)



    def test_np_array(self):
        arr = np.array([3,2,1,5,5,1,3])
        qs = QuickSort(arr)
        qs.sort()
        print(arr)



    def test_merge_sort(self):
        arr = [4,2,3,1]
        ms = MergeSort(arr)
        ms.sort()
        self.is_sorted(ms.data)

    def test_merge_sort_random(self):
        self.perform_random_test(MergeSort)

    def test_radix_sort(self):
        arr = [405, 246, 328, 2]
        rs = RadixSort(arr)
        rs.sort()
        self.is_sorted(rs.data)

    def test_get_digit(self):
        arr = [405, 246, 328]
        rs = RadixSort(arr)
        self.assertEqual(rs.get_digit(405, 0), 5)
        self.assertEqual(rs.get_digit(405, 1), 0)
        self.assertEqual(rs.get_digit(405, 2), 4)

        self.assertEqual(rs.get_digit(1298172, 4), 9)

    
    def test_radix_sort_random(self):
        radix_range = 10000000000000
        self.perform_random_test(RadixSort, radix_range, max_num_digits=len(str(radix_range)))

    def test_efficient_radix_sort(self):
        arr = [405, 246, 328, 2]
        rs = RadixSortEfficient(arr, 3)
        rs.sort()
        self.is_sorted(rs.data)

    def test_radix_sort_efficient_random(self):
        radix_range = 10000000000000
        self.perform_random_test(RadixSortEfficient, radix_range, max_num_digits=len(str(radix_range)))

if __name__ == '__main__':
    unittest.main()
