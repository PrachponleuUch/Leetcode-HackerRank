class Solution(object):
    def minPartitions(self, n):
        listn = list(n)
        r = int(listn[0])
        for i in range(len(listn) - 1):
            if r < int(listn[i+1]):
                r = int(listn[i+1])
        return r
        """
        :type n: str
        :rtype: int
        """