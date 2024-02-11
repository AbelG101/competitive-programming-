class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        max_amount = len(nums) // 3
        nums_hashmap = {}
        result = set()

        for num in nums:
            nums_hashmap[num] = nums_hashmap.get(num, 0) + 1
            if nums_hashmap[num] > max_amount:
                result.add(num)

        return result