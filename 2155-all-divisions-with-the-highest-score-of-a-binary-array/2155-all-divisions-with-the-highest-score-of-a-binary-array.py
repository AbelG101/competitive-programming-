class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # initialize prefix sum arrays to count zeros & ones.
        # loop through the array to calculate prefix sums for zeros & ones.
        # find the maximum division score & record indices achieving this score.
        # update max score & create a new set with the index of the maximum score.
        # if current score is the same as max, add the current score index to the set.
        # return the set of indices with highest division score.


        n = len(nums)
        zeros_prefix_sum = [0] * (n + 1)
        ones_prefix_sum = [0] * (n + 1)
        
        # calculate prefix sum arrays
        for i in range(1, n + 1):
            zeros_prefix_sum[i] = zeros_prefix_sum[i - 1] + (nums[i - 1] == 0)
            ones_prefix_sum[i] = ones_prefix_sum[i - 1] + (nums[i - 1] == 1)
        
        max_score = 0
        max_indices = set()
        
        # find max division score and record indices
        for i in range(n + 1):
            score = zeros_prefix_sum[i] + ones_prefix_sum[n] - ones_prefix_sum[i]
            if score > max_score:
                max_score = score
                max_indices = {i}
            elif score == max_score:
                max_indices.add(i)
        
        return max_indices

        