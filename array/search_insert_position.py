# Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index
# if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
def searchInsert(nums, target):
    low = 0
    high = len(nums) -1
    mid = 0

    while(low < high):
        mid = int(( low + high ) / 2)

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1

    return mid


print(searchInsert([1,3,5,6], 6))
