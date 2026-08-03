"""
binary_search.py

This program implements the binary search algorithm.

NOTE: Binary search only works on sorted arrays
"""
import random

SIZE = 1000000

def main():
    arr = [i for i in range(1, SIZE + 1)]
    target = random.randint(1, SIZE + 1)
    idx = binary_search(arr, target)

    if idx != -1:
        print(f'Target found at index: {idx}')
    else:
        print('Target not found')



def binary_search(arr, target) -> int:
    """
    This function implements the binary search algorithm to find the index
    of the target value.

    Args:
        arr (list): A sorted list of elements to search.
        target: The value to search for in the list.
    
    Returns:
        int: The index of the target value if found, otherwise -1.
    """

    start_idx = 0
    end_idx = len(arr) - 1


    while start_idx <= end_idx:
        # calculate the middle index of the current search range
        middle = ( start_idx + (end_idx - start_idx) // 2)

        print(f'Middle: {arr[middle]}')

        # if the target is in the lower half of the array
        if arr[middle] < target:
            start_idx = middle + 1

        # if the target is in the upper half of the array
        elif arr[middle] > target:
            end_idx = middle - 1

        else:
            return middle

    # target not found
    return -1


if __name__ == "__main__":
    main()