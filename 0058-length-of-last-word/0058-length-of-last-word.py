class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = -1
        result = ""
        s = s.strip()
        n = len(s)

        while(-i <= n and s[i] != " "):
            result += s[i]
            i -= 1

        return len(result)
        