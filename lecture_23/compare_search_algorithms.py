import random
import time

from search_utils import search_in_array
from search_utils import search_in_binary_tree
from search_utils import search_in_hashmap
from utils import convert_array_to_hashmap
from utils import convert_array_to_tree


def prepare_array(size: int) -> list:
    array = [i + 1 for i in range(size)]
    random.shuffle(array)
    return array


def measure_time(search_func, array) -> None:
    elems_to_find = (1, 1000, 100000, 100000000000000000)
    start = time.time()
    for element in elems_to_find:
        result = search_func(element, array)
        print(f"Element {element} is in array: {result}")
    end = time.time()
    print(f"Search time: {end - start}")


def main():
    print("Preparing array")
    array = prepare_array(10000000)
    print("Start search in array")
    measure_time(search_in_array, array)

    print("Start building tree")
    tree_array = convert_array_to_tree(array)
    print("Start search in binary tree")
    measure_time(search_in_binary_tree, tree_array)

    print("Start building hashmap")
    hashmap_array = convert_array_to_hashmap(array)
    print("Start search in hashmap")
    measure_time(search_in_hashmap, hashmap_array)


if __name__ == "__main__":
    main()
