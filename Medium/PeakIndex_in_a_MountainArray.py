class Solution(object):
    def peakIndexInMountainArray(self, arr):
        for i in range (1, len(arr) - 1):
            if (arr[i - 1] < arr[i]) and (arr[i] > arr[i + 1]):
                return i

        """
        :type arr: List[int]
        :rtype: int
        """
        