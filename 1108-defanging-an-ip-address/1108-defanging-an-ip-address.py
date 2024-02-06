class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        defanged_address = ""
        for character in address:
            if character == ".":
                defanged_address += "[.]"
            else: defanged_address += character
        
        return defanged_address
        