class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        my_set = set(fronts + backs)
        def is_good(current_card):
            for front_card, back_card in zip(fronts, backs):
                if front_card == back_card == current_card:
                    return False
            return True

        for card in sorted(my_set):
            if is_good(card):
                return card

        return 0
        