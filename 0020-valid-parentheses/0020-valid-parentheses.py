class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parentheses_map = {'{':'}', '[':']', '(':')'}
        # iterate over s
        for parentheses in s:
            # check if it's a closing parentheses
            if parentheses not in parentheses_map:
                # if there's no item on the stack return False
                if len(stack) == 0:
                    return False
                # check the type and compare it to the item on the stack
                # if they're not similar type return False
                if parentheses != parentheses_map[stack.pop()]:
                    return False
            # else add to the stack
            else: stack.append(parentheses)
        return len(stack) == 0
        