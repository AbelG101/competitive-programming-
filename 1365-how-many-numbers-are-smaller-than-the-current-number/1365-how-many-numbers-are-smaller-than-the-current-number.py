class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = sorted(nums)
        hm = {}
        res = []
        n = len(nums)

        for i in range(n):
            if temp[i] not in hm:
                hm[temp[i]] = i
        
        for i in range(n):
            res.append(hm[nums[i]])

        return res


        