"""
Given array of numbers.
Add up all the numbers and return the total.
Base Case: Array with 0 or 1 element
Recursive Case: Need to move closer to an empty array
with every recursive call.
Remember, recursion keeps track of the state (refer to readings on call stack)
Tip: when writing a recursive function involving an array,
the base case is often an empty array or an array with one element
Side Note: functional programs such as Haskell do not have loops so forced to use recursion instead
"""


def sum_arr(nums):
    if not nums:
        return 0
    return nums[0] + sum(nums[1:])

print('\nSummed total, given array [2, 4, 6] equals: ', sum_arr([2, 4, 6]), "\n")

print('Summed total, given array [] equals: ', sum_arr([]), "\n")

print('Summed total, given array [3] equals: ', sum_arr([3]), "\n")
