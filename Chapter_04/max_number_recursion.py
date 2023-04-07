'''
Recursive Function to find Max
Number in an Array
'''


def max_arr(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]
    sub_max = max(nums[1:])
    return nums[0] if nums[0] > sub_max else sub_max


print('\nItem count, given array [2, 4, 6] equals: ', max_arr([2, 4, 6]), "\n")

print('Item count, given array [] equals: ', max_arr([]), "\n")

print('Item count, given array [3] equals: ', max_arr([3]), "\n")
