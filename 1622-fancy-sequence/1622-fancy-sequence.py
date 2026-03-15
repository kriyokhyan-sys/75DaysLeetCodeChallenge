class Fancy(object):

    def __init__(self):
        self.nums = []
        self.mul = 1
        self.add = 0
        self.mod = 10**9 + 7

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        inv_mul = pow(self.mul, self.mod - 2, self.mod)
        self.nums.append(((val - self.add) * inv_mul) % self.mod)

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        self.add = (self.add + inc) % self.mod

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        self.mul = (self.mul * m) % self.mod
        self.add = (self.add * m) % self.mod

    def getIndex(self, idx):
        """
        :type idx: int
        :rtype: int
        """
        if idx >= len(self.nums):
            return -1
        return (self.nums[idx] * self.mul + self.add) % self.mod


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)