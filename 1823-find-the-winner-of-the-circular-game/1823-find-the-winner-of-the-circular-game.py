class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        result = 0
        for i in range(1, n + 1):
            result = (result + k) % i
        return result + 1
        