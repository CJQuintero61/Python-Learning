# Quicksort

Quicksort is a recursive algorithm that uses a divide and conquer strategy to sort
an array.

The algorithm requires 2 functions:

- quicksort
- partition

The quicksort function takes 3 arguments

- array (list) - the list to sort in place
- start_idx (int) - the index of first element in the list/partition
- end_idx (int) - the index of the last element in the list/partition

This function will be called by outside callers to sort a list in place and is the main interface.
It requires the aformentioned parameters, and makes a call to partition(array, start, end), then
recursively calls the quicksort function on the left half of the array (excluding the pivot) and the
right half of the array (excluding the pivot). The base case is when the end_idx is less than or
equal to the start_idx, where the function simply returns.

The other function is not meant to be called by outside callers, only by the quicksort function and
actually implements the logic for the algorithm. It uses 2 variables to traverse the array, i and j.
i will start at start_idx - 1, and j will start at the start_idx. We will also define a variable
called pivot_idx and set it to the last element in the list. We then use j to linearly traverse the array
until a value that is less than the pivot is found. When this happens, we increment i by 1, then perform a swap
between i and j using a temporary variable. After j has traversed all elements, we increment i by 1,
then perform a variable swap between i and the pivot, causing the pivot to now be in its proper place.
Then we return i back to the quicksort function.

```Python
def quicksort(array, start_idx, end_idx) -> None:
    """
    This function is the interface for the quicksort algorithm

    Args:
        array (list) - the array to sort in place
        start_idx (int) - the index of the first element in the array/partition
        end_idx (int) - the index of the last element in the array/partition

    Returns:
        None - the array is sorted in place
    """

    # base case
    if end_idx <= start_idx:
        return
    
    else:
        pivot_idx = _partition(array, start_idx, end_idx)   # move the pivot to the middle of the array
        quicksort(array, start_idx, pivot_idx - 1)          # sort the left half
        quicksort(array, pivot_idx + 1, end_idx)            # sort the right half
    

def _partition(array, start_idx, end_idx) -> int:
    """
    The function implements the quicksort algorithm logic. This function is not meant
    to be called by outside callers.

    Args:
        array (list) - the array to sort in place
        start_idx (int) - the index of the first element in the array/partition
        end_idx (int) - the index of the last element in the array/partition

    Returns:
        int - the pivot index after it has been placed in its proper position
    """
    
    i = start_idx - 1
    j = start_idx
    pivot_value = array[end_idx]

    while j <= end_idx - 1:
        
        if array[j] < pivot_value:
            i = i + 1

            temp_value = array[i]
            array[i] = array[j]
            array[j] = temp_value
        
        j = j + 1
    
    i = i + 1
    temp_value = array[i]
    array[i] = array[end_idx]
    array[end_idx] = temp_value

    return i
```
