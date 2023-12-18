class Solution(object):
    def findArray(self, pref):
        ans = [None] * len(pref)
        ans[0] = pref[0]
        for i in range(1, len(pref)):
            ans[i] = pref[i]^pref[i-1]
        return ans
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        