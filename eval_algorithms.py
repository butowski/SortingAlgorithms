from QuickSort import QuickSort
from BubbleSort import BubbleSort
import numpy as np
import time
from matplotlib import pyplot as plt



if __name__ == "__main__":


    #Profiling the different sorting algorithms

    rng = np.random.default_rng(12345)
    data = rng.integers(0,5000,10000)


    quick_sort = QuickSort(data)
    bubble_sort = BubbleSort(data)

    # evaluate quick sort
    start = time.perf_counter()
    quick_sort.sort()
    end = time.perf_counter()
    quick_sort_time = end-start
    print("QuickSort took {} seconds".format(quick_sort_time))

    #evaluate bubble sort
    start = time.perf_counter()
    bubble_sort.sort()
    end = time.perf_counter()
    bubble_sort_time = end-start
    print("BubbleSort took {} seconds".format(bubble_sort_time))

    #Plotting the different sorting algorithms
    fig, ax = plt.subplots()
    algorithms = ['QuickSort', 'BubbleSort']
    times = [quick_sort_time, bubble_sort_time]
    bar_labels = ["QuickSort", "BubbleSort"]
    ax.bar(algorithms, times, label=bar_labels)
    ax.set_ylabel("Execution Time")
    ax.set_xlabel("Algorithm")
    ax.set_title("Execution Time of Sorting algorithms")

    plt.show()
