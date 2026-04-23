import numpy as np

def merge_sort(array):
    """Sorts an array in-place using the merge sort algorithm.

    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left_array = np.empty(middle, dtype=int)
    right_array = np.empty(len(array) - middle, dtype=int)

    for i in range(len(array)):
        if(i < middle):
            left_array[i] = array[i]
        else:
            right_array[i - middle] = array[i]

    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)
    merge(left_array, right_array, array)

    return array

def merge(left_array, right_array, array):
    """Merges two sorted arrays into a single sorted array in-place."""
    size_left = len(left_array)
    size_right = len(right_array)
    i, l, r = 0, 0, 0

    while(l < size_left and r < size_right):
        if(left_array[l] <= right_array[r]):
            array[i] = left_array[l]
            l += 1
            i += 1
        else:
            array[i] = right_array[r]
            r += 1
            i += 1

    while(l < size_left):
        array[i] = left_array[l]
        l += 1
        i += 1

    while(r < size_right):
        array[i] = right_array[r]
        r += 1
        i += 1

if __name__ == "__main__":
    unsorted_numbers = np.random.randint(1, 10, 10)
    sorted_numbers = merge_sort(unsorted_numbers)
    print(sorted_numbers)