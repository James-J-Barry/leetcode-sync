class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = set()
        total = 0
        for num in nums:
            if not num in dic:
                dic.add(num)
        while dic:
            num = dic.pop()
            temp = 1
            current = num
            while current + 1 in dic:
                dic.remove(current + 1)
                current += 1
                temp += 1
            current = num
            while current - 1 in dic:
                dic.remove(current - 1)
                current -= 1
                temp += 1
            if temp > total:
                total = temp
        return total