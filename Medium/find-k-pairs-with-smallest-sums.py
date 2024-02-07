import heapq
def kSmallestPairs(nums1, nums2, k):
    n = len(nums1)
    m = len(nums2)
    pq = []
    hashSet = set()
    ans = []
    heapq.heappush(pq, (nums1[0] + nums2[0], 0, 0))
    hashSet.add((0, 0))
    while pq and k > 0:
        min_val, i, j = heapq.heappop(pq)
        ans.append([nums1[i], nums2[j]])
        if i < n - 1 and (i + 1, j) not in hashSet:
            heapq.heappush(pq, (nums1[i + 1] + nums2[j], i + 1, j))
            hashSet.add((i + 1, j))
        if j < m - 1 and (i, j + 1) not in hashSet:
            heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
            hashSet.add((i, j + 1))
        k -= 1
    return ans
  