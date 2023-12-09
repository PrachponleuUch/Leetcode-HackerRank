import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        low, high = 1, max(piles)
        if h == len(piles):
            return high
        while low <= high:
            mid = (low + high) // 2
            if sum(math.ceil(float(pile)/mid) for pile in piles) > h:
                low = mid + 1
            else: 
                high = mid - 1
        
        return low