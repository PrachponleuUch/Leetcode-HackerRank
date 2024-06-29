class Solution(object):
    def twoSum(self, nums, target):
        for idx, num in enumerate(nums):
            for i in range(idx + 1, len(nums)):
                if num + nums[i] == target:
                    return [idx, i]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        