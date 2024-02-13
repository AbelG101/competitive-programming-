class Solution(object):
    
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = len(nums) - 1
        j = i - 1
        k = j - 1

        nums.sort()

        while k > -1:
            is_valid = nums[i] + nums[j] > nums[k] and nums[i] + nums[k] > nums[j] and nums[j] + nums[k] > nums[i]
            if is_valid:
                return nums[i] + nums[j] + nums[k]
            i -= 1
            j -= 1
            k -= 1

        return 0
        