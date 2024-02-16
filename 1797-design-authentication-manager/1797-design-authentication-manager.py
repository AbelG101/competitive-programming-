class AuthenticationManager(object):

    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.timeToLive = timeToLive
        self.tokens_hm = {}
        

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        self.tokens_hm[tokenId] = currentTime + self.timeToLive
        

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """

        isValid = self.validateRenewRequest(tokenId, currentTime)
        if isValid:
            self.tokens_hm[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """

        count = 0
        for expiryTime in self.tokens_hm.values():
            if expiryTime > currentTime: count += 1

        return count

    def validateRenewRequest(self, tokenId, currentTime):
        if tokenId in self.tokens_hm and self.tokens_hm[tokenId] > currentTime:
            return True
        return False
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)