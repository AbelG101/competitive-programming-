class Solution:
    # function to calculate manhatan distance not euclidean
    def calc_distance(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        return abs(x2-x1) + abs(y2-y1)

    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        my_init_coordinate = [0, 0]
        my_distance_from_target = self.calc_distance(my_init_coordinate, target)

        for ghost_coordinate in ghosts:
            ghost_distance_from_target = self.calc_distance(ghost_coordinate, target)
            if ghost_distance_from_target <= my_distance_from_target:
                return False

        return True

        