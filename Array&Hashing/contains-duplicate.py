import collections
class Solution(object):
    def containsDuplicate(self, nums):
        return True if max(collections.Counter(nums).values()) > 1 else False
        """
        :type nums: List[int]
        :rtype: bool
        """

# Optimized
def containsDuplicate(nums):
  hashset = set()
  for num in nums:
    if num in hashset:
      return True
    hashset.add(num)
  return False
