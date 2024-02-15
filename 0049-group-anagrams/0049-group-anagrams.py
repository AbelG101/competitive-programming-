from collections import Counter
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        strings_hm = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))

            if sorted_string in strings_hm:
                strings_hm[sorted_string].append(string)
            else:
                 strings_hm[sorted_string] = [string]

        return strings_hm.values()