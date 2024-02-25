class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 4 pointer approach referenced from Neetcode on YT 
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        result = []

        while left < right and top < bottom:
            # go from left to right
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            # go from top to down
            for i in range(top, bottom):
                result.append(matrix[i][right-1])
            right -= 1

            # check if the matrix is a single row or single column
            if not (left < right and top < bottom):
                break

            # go from right to left
            for i in range(right-1, left-1, -1):
                result.append(matrix[bottom-1][i])
            bottom -= 1

            # go from bottom to top
            for i in range(bottom-1, top-1, -1):
                result.append(matrix[i][left])
            left += 1
            
        return result
