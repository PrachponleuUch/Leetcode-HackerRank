class Solution(object):
    def topKFrequent(self, nums, k):
        # Bucket Sort
        count = {}
        freq = [[] for i in range(1+ len(nums))]
        result = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, c in count.items():
            freq[c].append(num)

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        