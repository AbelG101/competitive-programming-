import random

class RandomizedSet(object):

    def __init__(self):
        self.nums_hashmap = {}
        self.nums_list = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.nums_hashmap:
            self.nums_list.append(val)
            self.nums_hashmap[val] = len(self.nums_list) - 1
            return True

        return False
        
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.nums_hashmap:
            idx = self.nums_hashmap[val]
            self.nums_list[idx] = self.nums_list[-1]
            self.nums_hashmap[self.nums_list[-1]] = idx
            self.nums_list.pop()
            del self.nums_hashmap[val]
            return True
        return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.nums_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()