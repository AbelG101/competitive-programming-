class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        i, j = 0, len(piles) - 1
        piles.sort(reverse = True)
        max_coins = 0
        
        while(i < j):
            i += 1 # skip alice's turn
            max_coins += piles[i] # add your current pile
            i += 1 # move to alice's turn
            j -= 1 # skip bob's turn

        return max_coins
