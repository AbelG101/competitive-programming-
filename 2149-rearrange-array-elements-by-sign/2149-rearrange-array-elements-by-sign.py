class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        negatives = []
        positives = []
        result = []

        for num in nums:
            if num > 0:
                positives.append(num)
            else: negatives.append(num)

        for pos, neg in zip(positives, negatives):
            result.extend([pos, neg])

        return result
        