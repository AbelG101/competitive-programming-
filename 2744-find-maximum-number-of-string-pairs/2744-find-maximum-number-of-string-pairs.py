class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        my_set = set()
        max_pairs = 0

        for word in words:
            if word in my_set:
                max_pairs += 1
            else: my_set.add(word[::-1])

        return max_pairs
        