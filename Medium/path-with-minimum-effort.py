class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        visited = set()
        minHeap = [[0,0,0]]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        while minHeap:
            diff, row, col = heapq.heappop(minHeap)
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if (row, col) == (rows-1, cols-1):
                return diff
            for r, c in directions:
                newRow, newCol = row + r, col + c
                if 0 <= newRow < rows and 0 <= newCol < cols:
                    newDiff = max(diff, abs(heights[row][col] - heights[newRow][newCol]))
                    heapq.heappush(minHeap, [newDiff, newRow, newCol])