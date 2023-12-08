class Solution(object):
    def peakIndexInMountainArray(self, arr):
        return arr.index(max(arr))

        """
        :type arr: List[int]
        :rtype: int
        """
        