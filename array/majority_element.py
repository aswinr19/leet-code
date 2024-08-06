# Majority Element (169, array, easy)

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3


def majorityElement(nums):

        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        for key, value in count.items():
            if value >  len(nums) / 2:
                return key

print(majorityElement([3,2,3]))
