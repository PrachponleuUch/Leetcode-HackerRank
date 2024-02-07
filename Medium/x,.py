import heapq, itertools
def kSmallestPairs(nums1, nums2, k):
    array = map(lambda u: ([u+v, u, v] for v in nums2), nums1)
    minHeap = heapq.merge(*array)
    return [sumUV[1:] for sumUV in itertools.islice(minHeap, k)]

print(kSmallestPairs([1,7,11], [2,4,6], 3))
  