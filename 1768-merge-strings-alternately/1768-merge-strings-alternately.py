class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # get length of the shotest word & get the longest word
        shortest_len, longest_word = [len(word1), word2] if len(word1) < len(word2) else [len(word2), word1]
        merged_str = ""
        i = 0
        
        # iterate & merge the strings
        while i < shortest_len:
            merged_str += word1[i]
            merged_str += word2[i]
            i += 1

        # check if there are letters left & append to the last
        while i < len(longest_word):
            merged_str += longest_word[i]
            i += 1

        return merged_str
        