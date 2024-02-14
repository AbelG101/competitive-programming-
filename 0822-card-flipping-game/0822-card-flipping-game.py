class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        unique_cards = set(fronts + backs)
        for card in sorted(unique_cards):
            if all(front != card or back != card for front, back in zip(fronts, backs)):
                return card
        return 0
        