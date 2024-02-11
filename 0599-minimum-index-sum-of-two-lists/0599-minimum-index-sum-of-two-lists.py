class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        hashmap = {}
        common_strings = []
        least_index_sum = float('inf')

        shortest_list, longest_list = (list1, list2) if len(list1) < len(list2) else (list2, list1)

        for idx, string in enumerate(longest_list):
            hashmap[string] = idx

        for idx, string in enumerate(shortest_list):
            if string in hashmap:
                index_sum = hashmap[string] + idx
                if index_sum < least_index_sum:
                    common_strings = [string]
                    least_index_sum = index_sum
                elif index_sum == least_index_sum:
                    common_strings.append(string)

        return common_strings
        