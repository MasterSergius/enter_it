import math


def convert_array_to_tree(array: list) -> list:
    r"""
    Permutate elements of array to simulate a balanced binary tree.

    Example 1:

          5
         / \
        3   7
       / \ / \
      1  4 6  9

    This tree might be represented as an array: [5, 3, 7, 1, 4, 6, 9]

    Example 2:

          5
         / \
        3   7
         \ / \
         4 6  9

    This tree might be represented as an array: [5, 3, 7, None, 4, 6, 9]
    """

    if not array:
        return []

    # sort array
    array_copy = array[:]
    array_copy.sort()
    n = len(array_copy)

    # 2. Calculate the maximum index we might need.
    # For a balanced tree, height h = ceil(log2(n+1)).
    # Max index is 2^h - 1.
    h = math.ceil(math.log2(n + 1)) + 1  # +1 for safety with uneven splits
    max_size = 2**h
    tree_array = [None] * max_size

    def fill_indices(start, end, target_idx):
        if start > end:
            return

        # Pick the middle
        mid = (start + end) // 2

        # Place value in the mathematical slot
        if target_idx < max_size:
            tree_array[target_idx] = array_copy[mid]

        # Recurse with 2i+1 and 2i+2
        fill_indices(start, mid - 1, 2 * target_idx + 1)
        fill_indices(mid + 1, end, 2 * target_idx + 2)

    fill_indices(0, n - 1, 0)

    # Trim the trailing Nones for a cleaner look
    while tree_array and tree_array[-1] is None:
        tree_array.pop()

    return tree_array


def convert_array_to_hashmap(array: list) -> list:
    """
    Simulate hashmap via sorted array

    It should contain only positive numbers like indexes, i.e. index = element
    """
    if not array:
        return []

    # sort array
    array_copy = array[:]
    array_copy.sort()

    # in case we don't have a strict sequence like 1,2,3..n, we need to use placeholders
    min_elem = array_copy[0]
    max_elem = array_copy[-1]

    result_array = []
    result_index = 0
    while result_index < min_elem:
        result_array.append(False)
        result_index += 1

    array_index = 0
    while result_index < max_elem:
        if result_index == array_copy[array_index]:
            result_array.append(True)
        else:
            result_array.append(False)
        result_index += 1
        array_index += 1

    return result_array
