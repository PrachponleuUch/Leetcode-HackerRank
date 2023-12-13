class Solution(object):
    def shipWithinDays(self, weights, days):
        def helper(mid):
            count, current_days = 0, 1
            for w in weights:
                count += w 
                if count > mid:
                    current_days += 1
                    count = w
            return current_days <=  days
        
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            if helper(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        