class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        middle_idx = n
        shuffled_list = []
        
        for i in range(middle_idx):
            shuffled_list.extend([nums[i], nums[i + middle_idx]])
            
        return shuffled_list