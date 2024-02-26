class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverse(word):
            return word[::-1]
        
        words = s.split()
        n = len(words)

        for i in range(n):
            words[i] = reverse(words[i])

        return ' '.join(words)

        