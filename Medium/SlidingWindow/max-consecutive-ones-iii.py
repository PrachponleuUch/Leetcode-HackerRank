class Solution(object):
    def longestOnes(self, nums, k):
        hash = {}
        l, ans = 0, 0
        for r, num in enumerate(nums):
            if num not in hash:
                hash[num] = 0
            hash[num] += 1
            if 0 in hash:
                while hash[0] > k:
                    hash[nums[l]] -= 1
                    l += 1
            cur_window_size = r - l + 1
            ans = max(ans, cur_window_size)
        return ans
            
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        