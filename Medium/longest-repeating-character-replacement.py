class Solution(object):
    def characterReplacement(self, s, k):
        hash = {}
        longestC, maxLength = 0, 0
        for i in range(len(s)):
            if not s[i] in hash:
                hash[s[i]] = 0
            hash[s[i]] += 1
            longestC = max(longestC, hash[s[i]])
            if maxLength - longestC >= k:
                hash[s[i - maxLength]] -= 1
            else:
                maxLength += 1 
        return maxLength
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        