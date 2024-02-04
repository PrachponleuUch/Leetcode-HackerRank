class Solution(object):
    def maximumTastiness(self, price, k):
        price.sort()
        l, h = 0, max(price)

        def condition(m):
            n = len(price)
            count = 1
            starter = price[0]
            for i in range(1,n):
                if  price[i] - starter >= m:
                    starter = price[i]
                    count += 1
            return count >= k
                
        while l <= h:
            mid = l + (h - l) / 2
            if condition(mid):
                l = mid + 1
            else:
                h = mid - 1
        return h
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        