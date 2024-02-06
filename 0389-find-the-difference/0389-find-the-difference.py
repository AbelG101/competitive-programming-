class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hash_map = {}

        # add letters in s to the hashmap with occurrences count as value 
        for letter in s:
            if letter in hash_map:
                hash_map[letter] += 1
            else:
                hash_map[letter] = 1

        # find the letter in t that's not in the hashmap
        for letter in t:
            if not(letter in hash_map) or hash_map[letter] < 1:
                return letter
            else: hash_map[letter] -= 1
        return ""
        