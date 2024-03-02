class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _max = 0
        i = 0
        j = len(nums)-1

        nums.sort()

        while i < j:
            pair_sum = nums[i] + nums[j]
            if pair_sum > _max:
                _max = pair_sum
            
            i += 1
            j -= 1
        
        return _max