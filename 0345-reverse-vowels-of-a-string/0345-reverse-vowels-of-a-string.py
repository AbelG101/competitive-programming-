class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        input_vowels = []
        vowels_set = set("aeiouAEIOU")
        result = ""

        for char in s:
            if char in vowels_set:
                input_vowels.append(char)

        for char in s:
            if char in vowels_set:
                result += input_vowels.pop()
            else: result += char

        return result

        

        