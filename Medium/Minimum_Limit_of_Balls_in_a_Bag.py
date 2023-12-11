class Solution(object):
    def minimumSize(self, nums, maxOperations):
        def helper(mid):
            count = 0
            for num in nums:
                count += (num-1)//mid
            return (count <= maxOperations)

        low = 1
        high = max(nums)

        while low <= high:
            mid = (low + high) // 2
            if helper(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        