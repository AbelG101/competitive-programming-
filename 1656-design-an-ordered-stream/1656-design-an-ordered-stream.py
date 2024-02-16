class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.ptr = 0
        self.arr = [""] * n
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        insert_idx = idKey-1
        self.arr[insert_idx] = value
        self.update_ptr()

        return self.arr[insert_idx : self.ptr]
        
    def update_ptr(self):
        while(self.ptr < self.n and self.arr[self.ptr] != ""):
            self.ptr += 1

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)