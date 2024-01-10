from QuickSort import QuickSort
from BubbleSort import BubbleSort
from insertion_sort import InsertionSort
from radix_sort import RadixSort, RadixSortEfficient
import numpy as np
import time
from matplotlib import pyplot as plt

def perform_measurements(alg_list, num_measurements):
    for alg in alg_list:
        alg_obj = alg['alg']
        # calculate average over mutliple runs. Discard the first run
        avg = 0
        start = time.perf_counter()
        alg_obj.sort()
        end = time.perf_counter()
        for i in range(0,num_measurements):
            start = time.perf_counter()
            alg_obj.sort()
            end = time.perf_counter()
            avg = avg + (end - start)
        avg = avg / num_measurements
        alg['duration'] = avg
        

if __name__ == "__main__":
    #Profiling the different sorting algorithms
    list_length = 600
    num_measurements = 100
    rand_upper_bound = 10000000


    rng = np.random.default_rng(12345)
    data = rng.integers(0,rand_upper_bound,list_length)


    quick_sort = QuickSort(data.copy())
    quick_sort_opt = QuickSort(data.copy(), use_optimization=True)
    bubble_sort = BubbleSort(data.copy())
    insert_sort = InsertionSort(data.copy())
    radix_sort = RadixSort(data.copy(), max_num_digits=len(str(rand_upper_bound)))
    radix_sort_efficient = RadixSortEfficient(data.copy(), max_num_digits=len(str(rand_upper_bound)))

    measurements = [
        {'name': "QuickSort", 'alg': quick_sort, "duration": -1},
        {'name': "QuickSort Optimized", 'alg': quick_sort_opt, "duration": -1},
        {'name': "BubbleSort", 'alg' :  bubble_sort, "duration" : -1},
        {'name': "InsertionSort", 'alg': insert_sort, "duration" : -1},
        {'name': "RadixSort", 'alg': radix_sort, "duration" : -1},
        {'name': "RadixSort Memory Optimized", 'alg': radix_sort_efficient, "duration": -1}
    ]

    perform_measurements(measurements, num_measurements)


    #Plotting the different sorting algorithms
    fig, ax = plt.subplots()
    bar_labels = [alg['name'] for alg in measurements]
    times = [alg['duration'] for alg in measurements]

    ax.bar(bar_labels, times, label=bar_labels)
    ax.set_ylabel("Execution Time")
    ax.set_xlabel("Algorithm")
    ax.set_title("Avg Execution Time of Sorting algorithms len={}".format(list_length))

    plt.show()
