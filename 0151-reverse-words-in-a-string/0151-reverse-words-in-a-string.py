class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == " ":
            return ""
        return " ".join(reversed(s.split()))
        