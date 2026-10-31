class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        m = max(citations)
        hasmoretthan = [0] * (m + 1)
        l = len(citations)
        for i in range(l):
            hasmoretthan[citations[i]] += 1
        for i in range(m - 1, -1, -1):
            hasmoretthan[i] = hasmoretthan[i + 1] + hasmoretthan[i]
        h = 0
        while h < m and hasmoretthan[h + 1] >= h + 1:
            h += 1
        return h