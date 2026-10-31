class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = dict()
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        ave = set(freq.values())
        if len(ave) == len(freq):
            return True
        else:
            return False