class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = []
        for num in nums:
            while num >= len(counts):
                counts.append(0)
            counts[num] += 1
        print(counts)
        newcounts = []
        for i in range(0, len(counts)):
            newcounts.append(sum(counts[0:i]))
        print(newcounts)
        result = [0] * len(nums)
        for i in range(len(nums)):
            n = nums[i]
            result[i] = newcounts[n]
        return result