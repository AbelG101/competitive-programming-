class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        less_cntr = 0
        same_cntr = 0
        res = []

        for num in nums:
            if num < target:
                less_cntr += 1
            elif num == target:
                same_cntr += 1
        
        for _ in range(same_cntr):
            res.append(less_cntr)
            less_cntr += 1

        return res