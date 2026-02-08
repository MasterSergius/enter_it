import random
import time

from sort_algorithms import bubble_sort_1
from sort_algorithms import bubble_sort_2
from sort_algorithms import bubble_sort_optimized
from sort_algorithms import select_sort
from sort_algorithms import tim_sort


def prepare_array(size: int) -> list:
    array = [i + 1 for i in range(size)]
    random.shuffle(array)
    return array


def measure_time(sort_func, array) -> None:
    start = time.time()
    sorted_array = sort_func(array)
    # uncomment for debug purposes
    # print(sorted_array)
    end = time.time()
    print(f"Sort time: {end - start}")


def main():
    print("Preparing array")
    array = prepare_array(10000)
    print("Bubble sort, naive")
    measure_time(bubble_sort_1, array)

    print("Bubble sort, neighbours")
    measure_time(bubble_sort_2, array)

    print("Bubble sort, optimized")
    measure_time(bubble_sort_optimized, array)

    print("Select sort")
    measure_time(select_sort, array)

    print("Tim sort")
    measure_time(tim_sort, array)


if __name__ == "__main__":
    main()
