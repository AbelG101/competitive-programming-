class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # if not expressable as sum of 3 consec. nums return []
        if num % 3 != 0:
            return []

        middle_num = num / 3
        return [middle_num - 1, middle_num, middle_num + 1]