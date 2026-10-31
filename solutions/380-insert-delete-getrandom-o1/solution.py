class RandomizedSet(object):

    def __init__(self):
        self.theset = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.theset:
            return False
        else:
            self.theset.append(val)
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.theset:
            self.theset.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        l = len(self.theset)
        r = random.random()
        return self.theset[int(r * l)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()