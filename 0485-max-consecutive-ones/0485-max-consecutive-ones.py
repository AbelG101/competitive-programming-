class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_occurence = 0
        occurence = 0
        for num in nums:
            if num == 1:
                occurence += 1 
            else: occurence = 0
            
            if occurence > max_occurence:
                max_occurence = occurence
        
        return max_occurence
        