class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        i = l - 1
        lowestreachable = i
        while i >= 0:
            if i != lowestreachable:
                j = i
                notfound = True
                while j <= i + nums[i] and notfound:
                    if j == lowestreachable:
                        lowestreachable = i
                        notfound = False
                    j +=1
            i -= 1
        return (0 == lowestreachable)
        
        