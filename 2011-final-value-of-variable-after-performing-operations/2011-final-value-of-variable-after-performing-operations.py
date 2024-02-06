class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0

        for operation in operations:
            # define each operation using if-else & compare each operation in the list
            if operation == "X++" or operation == "++X":
                x += 1
            else:
                x -= 1
        
        return x

        