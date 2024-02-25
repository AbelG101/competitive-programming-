class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0]*n for _ in range(1, n+1)]
        left, right = 0, n
        top, bottom = 0, n

        num = 1
        while left < right and top < bottom:
            for i in range(left, right):
                result[top][i] = num
                num += 1
            top += 1

            for i in range(top, bottom):
                result[i][right-1] = num
                num += 1
            right -= 1

            for i in range(right-1, left-1, -1):
                result[bottom-1][i] = num
                num += 1
            bottom -= 1

            for i in range(bottom-1, top-1, -1):
                result[i][left] = num
                num += 1
            left += 1

        return result


        