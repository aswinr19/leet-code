# Missing Number (268, array, easy)

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
# 2 is the missing number in the range since it does not appear in nums.

def missingNumber(nums):

    nums.sort()

    if len(nums) == 1:
        if nums[0] == 0:
            return 1
        else:
            return 0
    else:
        if nums[0] != 0:
            return 0

    for i in range(0, len(nums)):
        if i > 0 and i < len(nums) and (nums[i] - nums[i-1]) != 1 :
            return nums[i -1] + 1

    return nums[len(nums) -1] +1
