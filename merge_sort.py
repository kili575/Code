import numpy as np 

unsorted_numbers = np.random.randint(1, 10, 10)

def merge_sort(array):
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
    
    merge_sort(left_array)
    merge_sort(right_array)
    merge(left_array, right_array, array)

def merge(left_array, right_array, array):
    