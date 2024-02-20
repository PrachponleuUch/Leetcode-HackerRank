import itertools
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        for i in range(n):
            arr.append(list(itertools.accumulate(nums[i:])))
        arr = list(itertools.chain.from_iterable(arr))
        arr.sort()
        return sum(arr[left-1:right]) % (10**9 + 7)
            