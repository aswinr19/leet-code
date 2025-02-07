# Merge Sorted Array (88, array, easy)

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and
# two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside
# the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements
# denote the elements that should be merged, and the last n elements are set to 0 and should be
# ignored. nums2 has a length of n.

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

def merge(nums1, m, nums2, n):

        for i in range(1, len(nums1) -m + 1):
            nums1.pop()

        for elm in nums2 :
            nums1.append(elm)

        nums1.sort()


num1 = [1,3,5,7,0,0,0]
num2 = [2,4,6]

merge(num1,4,num2,3)

print(num1)
