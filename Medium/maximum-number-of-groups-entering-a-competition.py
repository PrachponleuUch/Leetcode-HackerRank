import math
class Solution(object):
    def maximumGroups(self, grades):
        return int((-1 + math.sqrt(1-(4*2*(-len(grades)))))/2)
        """
        :type grades: List[int]
        :rtype: int
        """
        
        