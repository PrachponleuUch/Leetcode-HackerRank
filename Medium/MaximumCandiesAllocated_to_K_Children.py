class Solution(object):
    def maximumCandies(self, candies, k):
        low = 1
        high = sum(candies)//k
        while low <= high:
            mid = (low + high)//2
            counter = 0
            for candy in candies:
                    if mid <= candy:
                        counter += candy//mid
            if counter >= k:
                low = mid + 1
            else: 
                high = mid - 1
        return high
            
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        