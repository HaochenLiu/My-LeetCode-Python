class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums1 = nums
        nums2 = nums
        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                if j > i and num1 + num2 == target:
                    return (i, j)
