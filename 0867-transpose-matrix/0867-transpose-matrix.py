class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])

        result = [[0]*rows for i in range(cols)]

        for col in range(cols):
            for row in range(rows):
                result[col][row] = matrix[row][col]
        
        return result
        