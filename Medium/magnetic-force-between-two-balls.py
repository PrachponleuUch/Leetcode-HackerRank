class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 0, position[-1]
        def helper(x):
            start = position[0]
            count = 1
            for p in position:
                if p - start >= x:
                    start = p
                    count += 1
            return count >= m

        while l < r:
            mid = (l+r)//2
            if helper(mid + 1):
                l = mid + 1
            else:
                r = mid
        return r