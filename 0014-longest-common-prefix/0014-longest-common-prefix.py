class Solution(object):
    def find_common_prefix(self, str1, str2):
        # find length of shortest string
        str_len = len(str1) if len(str1) < len(str2) else len(str2) 
        common_prefix = ""
        
        for i in range(str_len):
            if str1[i] == str2[i]:
                common_prefix += str1[i]
            else: break
        return common_prefix
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # check if arr length is < 2 & return ""
        if len(strs) < 2:
            return strs[0]

        # find common prefix between the first two elts
        common_prefix = self.find_common_prefix(strs[0], strs[1])

        # check if arr length is < 3 & return common prefix var value
        if len(strs) < 3:
            return common_prefix

        # start from the 3rd elt in the arr compare with the cp var and iterate
        for i in range(2, len(strs)):
            common_prefix = self.find_common_prefix(strs[i], common_prefix)
        
        return common_prefix
        