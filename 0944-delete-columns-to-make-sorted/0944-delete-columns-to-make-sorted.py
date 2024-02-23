class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        cols = len(strs[0])
        rows = len(strs)

        deleted_cntr = 0

        for col in range(cols):
            for row in range(1, rows):
                if strs[row-1][col] > strs[row][col]:
                    deleted_cntr += 1
                    break
        
        return deleted_cntr