"""
quicksort.py

This script implements the quick sort algorithm. In this implementation,
the pivot is always the last element of the array.
"""
import random
import copy

# size of the array to be sorted
SIZE = 10

def main():

    # instead of writing unit tests, I tested a lot of randomly generated arrays
    for test_idx in range(10000):
        array = [random.randint(0, 100) for _ in range(SIZE)]

        # for testing the quicksort algorithm
        array_copy = copy.deepcopy(array)
        array_copy.sort()

        quicksort(array, 0, len(array) - 1)

        # assert the algorithm works
        assert array == array_copy, f"Test {test_idx} failed: {array} != {array_copy}"

        print(f"Test {test_idx} passed: {array} == {array_copy}")


def quicksort(array, start_idx, end_idx) -> None:
    """
    This function is the main function that implements the quick sort algorithm recursively.
    The pivot gets placed in its correct position in the sorted array,
    so we do not need to include the pivot index in the recursive calls.
    
    Args:
        array (list): The list of integers to be sorted.
        start_idx (int): The starting index of the sub-array to be sorted.
        end_idx (int): The ending index of the sub-array to be sorted.
    
    Returns:
        None: The array gets sorted in place, so there is no return value.
    """
    if end_idx <= start_idx:
        return

    else:
        partition_idx = _partition(array, start_idx, end_idx)   # find the partition index
        quicksort(array, start_idx, partition_idx - 1)          # recursively sort the left sub-array
        quicksort(array, partition_idx + 1, end_idx)            # recursively sort the right sub-array


def _partition(array, start_idx, end_idx) -> int:
    """
    Helper function for the quicksort function. 
    This function partitions the array into 2 sub arrays based on the pivot value

    Args:
        array (list): The list of integers to be sorted.
        start_idx (int): The starting index of the sub-array to be partitioned.
        end_idx (int): The ending index of the sub-array to be partitioned.
    
    Returns:
        int: The index of the pivot value after partitioning.
    """
    temp_value = None
    i = start_idx - 1
    j = start_idx

    # choose the last element as the pivot
    pivot_value = array[end_idx]

    # from the start idx to the end index - 1
    while j <= end_idx - 1:

        # when a value that is less than the pivot is found
        if array[j] < pivot_value:
            # increment i
            i = i + 1

            # swap i and j
            temp_value = array[i]
            array[i] = array[j]
            array[j] = temp_value

        # increment j
        j = j + 1

    # after j reaches the pivot's index
    i = i + 1

    # swap the pivot to i
    temp_value = array[i]
    array[i] = array[end_idx]
    array[end_idx] = temp_value

    # location of the pivot
    return i


if __name__ == "__main__":
    main()