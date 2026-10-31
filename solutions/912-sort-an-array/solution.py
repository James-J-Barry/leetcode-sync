class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # merge sort
        if len(nums) <= 1:
            return nums
        l = len(nums)
        lb, rb = nums[:int(l/2)], nums[int(l/2):]

        left, right = self.sortArray(lb), self.sortArray(rb) #check

        result = []
        i,j = 0,0
        while len(result) < len(nums):
            if i >= len(left):
                result.append(right[j])
                j += 1
            elif j >= len(right):
                result.append(left[i])
                i += 1
            elif left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        return result
