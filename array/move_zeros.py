# Move Zero's (283, array, easy)

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]


def moveZeroes(nums ):

    for elm in nums[:]:
        if elm == 0:
            nums.remove(elm)
            nums.append(0)
