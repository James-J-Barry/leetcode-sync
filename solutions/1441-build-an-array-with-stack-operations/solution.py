class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        n = 1
        result = []
        for num in target:
            while n < num:
                result.append("Push")
                result.append("Pop")
                n += 1
            result.append("Push")
            n += 1
        return result



