class Solution(object):
    def appendCharacters(self, s, t):
        sIdx, tIdx, sLen, tLen = 0, 0, len(s), len(t)
        while sIdx < sLen and tIdx < tLen:
            if (s[sIdx] == t[tIdx]):
                tIdx +=  1
            sIdx += 1
        return tLen - tIdx

        """
        :type s: str
        :type t: str
        :rtype: int
        """
        