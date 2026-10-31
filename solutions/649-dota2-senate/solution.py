class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        dire = deque()
        radiant = deque()

        for i in range(0, len(senate)):
            if senate[i] == 'D':
                dire.append(i)
            else:
                radiant.append(i)
        n = len(senate)
        while dire and radiant:
            d = dire.popleft()
            r = radiant.popleft()
            if d < r:
                dire.append(d + n)
                n += 1
            else:
                radiant.append(r + n)
                n += 1
        if radiant:
            return "Radiant"
        else:
            return "Dire"