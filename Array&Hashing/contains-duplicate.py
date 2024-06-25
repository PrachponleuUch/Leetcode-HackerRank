import collections
class Solution(object):
    def containsDuplicate(self, nums):
        return True if max(collections.Counter(nums).values()) > 1 else False
        """
        :type nums: List[int]
        :rtype: bool
        """
        