class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        removed_elts_cntr = 0
        for i in range(len(nums)):
            if nums[i] == val:
                removed_elts_cntr += 1
                nums[i] = 99
        nums.sort()
        return len(nums) - removed_elts_cntr
        