import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        h = max(nums)
        def helper(x):
            count = 0
            for num in nums:
                count = count + math.ceil(num/x)
            return count > threshold
        while l < h:
            mid = (l + h) // 2
            if helper(mid):
                l = mid + 1
            else:
                h = mid
        return h