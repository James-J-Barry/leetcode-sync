class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones_bef_zero = 0
        max_length = 0
        cur_length = 0
        first_zero = True
        for num in nums:
            if num == 0:
                if not first_zero:
                    cur_length -= ones_bef_zero
                    ones_bef_zero = cur_length
                else:
                    first_zero = False
                    ones_bef_zero = cur_length
            else:
                cur_length += 1
            if cur_length > max_length:
                max_length = cur_length
        if first_zero:
            max_length -= 1
        return max_length
        