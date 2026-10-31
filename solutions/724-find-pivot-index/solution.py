class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftsum = 0
        rightsum = 0
        length = len(nums)
        for n in range(1,length):
            rightsum += nums[n]
        if rightsum == 0:
            return 0
        for n in range(1,length):
            leftsum += nums[n-1]
            rightsum -= nums[n]
            if leftsum == rightsum:
                return n
        return -1
        