class Solution(object):
    def minDistance(self, str1, str2):
        memo = {}
  
        def recurse(i1, i2):
            key = i1, i2
            # Check if value has been calculated
            if key in memo:
                return memo[key]
            # Leftover characters in str2
            elif i1 == len(str1):
                memo[key] = len(str2) - i2
            # Leftover characters in str1
            elif i2 == len(str2):
                memo[key] = len(str1) - i1
            elif str1[i1] == str2[i2]:
                memo[key] = recurse(i1 + 1, i2 + 1)
            else:
                memo[key] = 1 + min(
                    recurse(i1 + 1, i2), # Delete
                    recurse(i1 + 1, i2 + 1), #Swap
                    recurse(i1, i2 + 1) #Insert
                )
            return memo[key]
        return recurse(0,0)
        