class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        current_pos = -1
        can_capacity = capacity
        steps = 0

        n = len(plants)

        for i in range(n):
            can_capacity -= plants[i]
            steps += i - current_pos 
            current_pos = i

            if i != n-1 and plants[i+1] > can_capacity:
                steps += current_pos + 1
                can_capacity = capacity
                current_pos = -1
        
        return steps