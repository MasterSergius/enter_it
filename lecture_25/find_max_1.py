import random


def find_max(array: list):
    # Space complexity - O(1)
    max_elem = array[0]
    for i in range(len(array)):
        if max_elem < array[i]:
            max_elem = array[i]

    return max_elem


def prepare_array(size: int) -> list:
    array = [random.randint(0, 100) for i in range(size)]
    return array


def main():
    array = prepare_array(10)
    print(f"Array: {array}")
    print(f"Max elem: {find_max(array)}")


if __name__ == "__main__":
    main()
