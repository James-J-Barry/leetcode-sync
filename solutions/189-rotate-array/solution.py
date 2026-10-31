class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        temp = [0] * l
        c = k % l
        i = c
        j = 0
        while i < l:
            temp[i] = nums[j]
            i +=1
            j +=1
        i = 0
        while j < l:
            temp[i] = nums[j]
            i +=1
            j +=1
        nums[:] = temp
        