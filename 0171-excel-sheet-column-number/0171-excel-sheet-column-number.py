class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        hm = {}
        n = len(columnTitle)
        result = 0

        for i in range(ord('A'), ord('Z') + 1):
            hm[chr(i)] = i - ord('A') + 1

        for i in range(n):
            result += hm[columnTitle[i]] * 26 ** (n - (i+1))

        return result
        