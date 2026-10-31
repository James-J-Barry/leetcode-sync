class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        j = 1
        lastNum = nums[0]
        count = 1
        l = len(nums)
        while i < l:
            if nums[i] == lastNum and count > 1:
                i += 1
            elif nums[i] == lastNum:
                count += 1
                nums[j] = nums[i]
                i += 1
                j += 1
            else:
                count = 1
                lastNum = nums[i]
                nums[j] = nums[i]
                i += 1
                j += 1
        return j
        