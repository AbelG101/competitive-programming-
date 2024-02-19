class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        concatenated_word = ""
        for word in words:
            concatenated_word += word
            if len(concatenated_word) > len(s):
                return False
            if s == concatenated_word:
                return True

        return False
