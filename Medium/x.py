import bisect
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def helper(word):
            hash = {}
            curr = word[0]
            hash[curr] = 0
            for s in word:
                if s == curr:
                    hash[s] += 1
                elif s != curr:
                    curr = s
                    if s in hash:
                        hash[s] += 1
                    else:
                        hash[s] = 1
            return hash[min(hash.keys())]
            
        qFreq = [helper(w) for w in queries]
        wFreq = sorted([helper(w) for w in words])
        n = len(wFreq)
        answer = []
        for q in qFreq:
            answer.append(n - bisect.bisect_right(wFreq, q))
        return answer