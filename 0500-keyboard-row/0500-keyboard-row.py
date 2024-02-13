class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        # hashmap = {"q" : 1, "w": 1, "e" : 1, "r", }

        hashmap = {}

        for char in first_row:
            hashmap[char] = 1

        for char in second_row:
            hashmap[char] = 2

        for char in third_row:
            hashmap[char] = 3

        result = []
        is_in_same_row = True
        for word in words:
            current_row = hashmap[lower(word[0])]
            for ch in word:
                if hashmap[lower(ch)] != current_row:
                    is_in_same_row = False
                    break
            if is_in_same_row:
                result.append(word)
            is_in_same_row = True

        return result