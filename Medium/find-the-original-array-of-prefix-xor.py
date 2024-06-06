class Solution(object):
    def findArray(self, pref):
        arr = [None] * len(pref)
        arr[0] = pref[0]
        for i in range(1, len(pref)):
            arr[i] = pref[i - 1] ^ pref[i]
        return arr

        """
        :type pref: List[int]
        :rtype: List[int]
        """
        