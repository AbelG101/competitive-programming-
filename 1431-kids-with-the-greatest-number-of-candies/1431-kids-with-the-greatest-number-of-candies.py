class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        greatest_number_of_candies = max(candies)
        n = len(candies)
        result = [False] * n

        for i in range(n):
            if candies[i] + extraCandies >= greatest_number_of_candies:
                result[i] = True
        return result
        