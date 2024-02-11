class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        result = [[], [], []]

        for num in nums:
            if num < pivot:
                result[0].append(num)
            elif num > pivot:
                result[2].append(num)
            else: result[1].append(num)

        return result[0] + result[1] + result[2] 
        