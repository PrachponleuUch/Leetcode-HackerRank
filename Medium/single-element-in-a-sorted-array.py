class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        for i in range(0, n - 2, 2):
            if ((nums[i] + nums[i+1])/2) != nums[i]:
                return nums[i]
        return nums[-1]