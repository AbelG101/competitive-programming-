class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        operations_hashmap = {}
        # iterate over reversed operations to skip intermediary replacements of similar items
        for to_be_replaced, replacement in reversed(operations):
            # check if the replacement is already replaced by another value previously
            operations_hashmap[to_be_replaced] = operations_hashmap.get(replacement, replacement)

        for i in range(len(nums)):
            if nums[i] in operations_hashmap:
                nums[i] = operations_hashmap[nums[i]]
        return nums