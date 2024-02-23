class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])

        # result matrice size should be cols x rows not the other way around
        result = [[0]*rows for i in range(cols)]

        # since we're transponsing loop should start from cols 
        for col in range(cols):
            for row in range(rows):
                result[col][row] = matrix[row][col]
        
        return result
        