class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        for idx in range(len(capacity)):
            capacity[idx] -= rocks[idx]
            
        capacity.sort()
        for idx in range(len(capacity)):
            if capacity[idx] > additionalRocks:
                return idx
            additionalRocks -= capacity[idx]
            
        return len(capacity)
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        