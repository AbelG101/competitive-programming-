class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letters_hm = {}
        for char in magazine:
            letters_hm[char] = letters_hm.get(char, 0) + 1

        
        for char in ransomNote:
            if char in letters_hm and letters_hm[char] > 0:
                letters_hm[char] -= 1
            else:
                return False
        
        return True
