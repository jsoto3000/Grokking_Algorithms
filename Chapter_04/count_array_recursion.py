'''
Recursive Function to Count
Number of items in an Array
'''


def count_arr(nums):
    if not nums:
        return 0
    return len(nums[0:])

print('\nItem count, given array [2, 4, 6] equals: ', count_arr([2, 4, 6]), "\n")

print('Item count, given array [] equals: ', count_arr([]), "\n")

print('Item count, given array [3] equals: ', count_arr([3]), "\n")