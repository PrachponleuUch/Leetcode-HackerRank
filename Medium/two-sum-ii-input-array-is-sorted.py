import bisect
class Solution(object):
    def twoSum(self, numbers, target):
        def BinarySearch(a, x):
            i = bisect.bisect_left(a, x)
            if i != len(a) and a[i] == x:
                return i
            else:
                return 0
        for i, num in enumerate(numbers):
            j = BinarySearch(numbers, target-num)
            if (num + numbers[j] == target):
                if (i == j):
                    return [i+1, j+2]
                else:
                    return [i+1, j+1]
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        