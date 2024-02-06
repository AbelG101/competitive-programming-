class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map = {}
        good_pairs_count = 0

        # add each elt to the hash map with count of occurence as value
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        
        # convert each occurence into pairs count & sum the total
        for value in hash_map.values():
            pairs_count = (value * (value - 1)) / 2
            good_pairs_count += pairs_count
        
        return good_pairs_count