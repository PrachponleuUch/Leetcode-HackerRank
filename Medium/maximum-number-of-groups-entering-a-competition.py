import math
# Method 1 (Quadratic Formula)
class Solution(object):
    def maximumGroups(self, grades):
        # return int((-1 + math.sqrt(1-(4*2*(-len(grades)))))/2)
        return int(math.sqrt(0.25 + 2*len(grades))-0.5)
        """
        :type grades: List[int]
        :rtype: int
        """
# Method 2 (Greedy)
# def maximumGroups(grades):
#   n = len(grades)
#   k = 0
#   while n >= k:
#     k += 1
#     n -= k
#   return k

# Method 3 (Binary Search)
# def maximumGroups(grades):
#   n = len(grades)
#   lo, hi = -1, n
#   while hi - lo > 1:
#     mid = (hi + lo + 1)//2
#     if (mid*(mid+1))//2 > n:
#       hi = mid
#     else:
#       lo = mid + 1
#   if (lo*(lo + 1))//2 <= n:
#     return lo 
#   return lo - 1
        