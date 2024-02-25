class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # SOLUTION 1: BY CONVERTING TO A STRING
        # num = int("".join(map(str, digits))) + 1
        # return [int(digit) for digit in str(num)]

        # iterate in reverse order
            # if at last digit or there's a previous remainder
                # check if last digit is 9, then replace it with 0 and set remainder exists to true
                # else then just add one to the last digit and set remainder exists to false

        
        n = len(digits)
        remainder_exists = False
        for i in range(n-1, -1, -1):
            if i == n-1 or remainder_exists:
                if digits[i] == 9:
                    digits[i] = 0
                    remainder_exists = True
                else:
                    digits[i] += 1
                    remainder_exists = False
        
        if remainder_exists:
            digits.insert(0, 1)
        
        return digits
    