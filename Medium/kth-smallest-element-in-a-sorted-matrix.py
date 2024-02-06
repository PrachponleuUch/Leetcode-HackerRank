import bisect
class Solution(object):
    def kthSmallest(self, matrix, k):
        l, h = matrix[0][0], matrix[-1][-1]
        def condition(m):
            count = 0
            for i in range(len(matrix)):
                x = bisect.bisect_right(matrix[i], m)
                count += x
            return count < k
        while l < h:
            mid = (h + l)//2
            if condition(mid):
                l = mid + 1
            else:
                h = mid
        return l
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        