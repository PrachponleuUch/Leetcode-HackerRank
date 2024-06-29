class Solution(object):
    def isAnagram(self, s, t):
        return (collections.Counter(list(s))) == (collections.Counter(list(t)))
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        