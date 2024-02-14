class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        answer = []
        n = len(boxes)
        for i in range(n):
            sum = 0
            for j in range(n):
                if boxes[j] != "0":
                    sum += abs(i-j)
            answer.append(sum)

        return answer

        