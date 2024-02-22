class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(img)
        cols = len(img[0])

        result = [[0] * cols for i in range(rows)]

        for row in range(rows):
            for col in range(cols):
                _sum = 0
                cntr = 0
                for i in range(row-1, row+2):
                    if i < 0 or i == rows:
                        continue
                    for j in range(col-1, col+2):
                        if j < 0 or j == cols:
                            continue 
                        _sum += img[i][j]
                        cntr += 1
                result[row][col] = _sum // cntr

        return result
        