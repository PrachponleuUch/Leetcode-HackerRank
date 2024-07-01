from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        seen = defaultdict(list)
        for str in strs:
            key = ''.join(sorted(str))
            seen[key].append(str)
        return list(seen.values())
                    
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        