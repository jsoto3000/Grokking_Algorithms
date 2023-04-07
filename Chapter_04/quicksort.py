'''
Recursive Quicksort (Ascending) Algorithm
Base Case is array with less than elements
'''

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        lesser = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    return quicksort(lesser) + [pivot] + quicksort(greater)


print('\nQuicksort, given array [10, 5, 2, 3]: ', quicksort([10, 5, 2, 3]), "\n")

print('Quicksort, given array []: ', quicksort([]), "\n")

print('Quicksort, given array [3]: ', quicksort([3]), "\n")

