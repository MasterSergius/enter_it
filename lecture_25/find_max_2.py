import random


def find_max(array: list):
    # Space complexity - O(1)
    # assume, we have at least 1 element
    max_elem = array[0]
    for i in range(len(array)):
        if max_elem < array[i]:
            max_elem = array[i]

    return max_elem


def get_all_elements(filename: str):
    # Space complexity - O(n)
    with open(filename) as f:
        data = f.readlines()
    return [int(elem) for elem in data]


def find_max_1(filename: str):
    return find_max(get_all_elements(filename))


def find_max_2(filename: str):
    # Space complexity - O(1)
    with open(filename) as f:
        first = True
        for line in f:
            # assume, we have at least 1 element
            elem = int(line)
            if first:
                max_elem = elem
                first = False
            if max_elem < elem:
                max_elem = elem

    return max_elem


def prepare_array(size: int) -> list:
    array = [random.randint(0, 100) for i in range(size)]
    return array


def create_array_and_write_to_file(size: int, filename: str):
    array = prepare_array(size)
    with open(filename, "w") as f:
        for elem in array:
            f.write(f"{elem}\n")


def main():
    filename = "array_of_ints.txt"
    create_array_and_write_to_file(10, filename)
    print(f"Max elem, O(n): {find_max_1(filename)}")
    print(f"Max elem, O(1): {find_max_2(filename)}")


if __name__ == "__main__":
    main()
