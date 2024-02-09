class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """

        losers_hashmap = {}
        winner_hashmap = {}
        not_lost_any_matches = []
        lost_one_match = []
        
        # iterate, get the value at index 1 and store in hasmap with occurence as value
        for match in matches:
            loser = match[1]
            losers_hashmap[loser] = losers_hashmap.get(loser, 0) + 1

        for match in matches:
            winner = match[0]
            loser = match[1]
            if losers_hashmap.get(winner) == None and winner_hashmap.get(winner, 0) < 1:
                not_lost_any_matches.append(winner)
                winner_hashmap[winner] = 1
            if losers_hashmap[loser] == 1:
                lost_one_match.append(loser)
            if winner_hashmap.get(winner, 0) == 1:
                winner_hashmap[winner] += 1

        not_lost_any_matches.sort()
        lost_one_match.sort()
        return [not_lost_any_matches, lost_one_match]

        # iterate, get the value at index 0 and check if it exists in the hm 
            # if it doesn't store in a list called lost...
            # if it does and occurence is 1 store in lost one matches
        