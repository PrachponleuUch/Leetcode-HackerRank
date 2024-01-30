class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        cF, cT, i, j, ans = 0, 0, 0, 0, 0
        while j < len(answerKey):
            if answerKey[j] == 'T':
                cT += 1
            else:
                cF += 1
            while (min(cT, cF) > k):
                if answerKey[i] == 'T':
                    cT -= 1
                else:
                    cF -= 1
                i += 1
            j += 1
            ans = max(ans, cT + cF)
        return ans
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        