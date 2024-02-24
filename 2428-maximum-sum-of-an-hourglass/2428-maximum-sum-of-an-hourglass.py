class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        max_sum = 0

        for row in range(rows-2):
            for col in range(cols-2):
                max_sum = max(max_sum, grid[row][col] + grid[row][col+1] + grid[row][col+2] + grid[row+1][col+1] + grid[row+2][col] + grid[row+2][col+1] + grid[row+2][col+2])

        return max_sum