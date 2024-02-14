class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}
        n = len(nums)

        for i in range(n):
            difference = target - nums[i]
            if difference in hm:
                return[i, hm[difference]]
            hm[nums[i]] = i

        return []
        