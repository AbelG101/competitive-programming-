class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = []

        _sum = 0
        for num in self.nums:
            _sum += num
            self.sums.append(_sum)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.sums[right] - self.sums[left-1] if (left > 0 and right > 0) else self.sums[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)