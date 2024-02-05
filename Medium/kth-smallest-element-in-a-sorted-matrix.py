class Solution(object):
    def kthSmallest(self, matrix, k):
        array = []
        for i in range(len(matrix)):
            array += matrix[i]
        array.sort()
        return array[k-1]
        
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        