def search_in_array(element: int, array: list) -> bool:
    """
    Return True if element exists in array, return False otherwise
    """
    result = False
    for item in array:
        if element == item:
            result = True
            break

    return result


def search_in_binary_tree(element: int, array: list) -> bool:
    """
    Return True if element exists in array, return False otherwise
    """
    index = 0
    result = False
    while index < len(array):
        # no element in array
        if array[index] is None:
            break

        # found element
        if element == array[index]:
            result = True
            break

        # move to next leaves
        if element < array[index]:
            index = 2 * index + 1
            continue
        if element > array[index]:
            index = 2 * index + 2
            continue
    return result


def search_in_hashmap(element: int, array: list) -> bool:
    """
    Return True if element exists in array, return False otherwise
    """
    if element > len(array) - 1:
        return False
    return array[element]
