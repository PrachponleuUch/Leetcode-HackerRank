class Solution(object):
    def minimizedMaximum(self, n, quantities):
        def helper(mid):
            count = 0
            for q in quantities:
            # If there's a remainder add 1, else 0 {True: 1, False: 0}
                count += (q//mid) + (q%mid > 0)
            return count <= n

        low = 1
        high = max(quantities)
        while low <= high:
            mid = (low + high) // 2
            if helper(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        