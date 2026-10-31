class RecentCounter(object):
    def __init__(self):
        self.pings = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.pings.append(t)
        i = 0
        while (self.pings[i] < t - 3000):
            self.pings.pop(i)
        return len(self.pings)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)