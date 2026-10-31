class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        i = 0
        j = n
        result = []
        while i < n or j < 2 * n:
            if (len(result) % 2) == 0:
                result.append(nums[i])
                i += 1
            else: 
                result.append(nums[j])
                j += 1
        return result