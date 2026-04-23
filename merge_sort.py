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
    size_left = len(array) // 2
    size_right = len(array) - size_left
    i, l, r = 0

    while(l < size_left & r < size_right):
        if(left_array[l] >= right_array[r]):
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