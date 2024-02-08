class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_set = {x for x in range(len(nums)+1)}

        for num in my_set:
            if num not in nums:
                return num
        