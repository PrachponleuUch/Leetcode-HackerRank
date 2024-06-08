class Solution(object):
    def countPoints(self, points, queries):
        cPoint = [0] * len(queries)
        for index, query in enumerate(queries):
            for point in points:
                if (query[0] - point[0])**2 + (query[1] - point[1])**2 <= (query[2])**2:
                    cPoint[index] += 1
        return cPoint

        
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
# Distance from center to point must be equal to or less than radius