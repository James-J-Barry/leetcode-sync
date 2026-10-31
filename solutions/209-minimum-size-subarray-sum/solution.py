class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        l = len(nums)
        minlength = l
        overallSum = 0
        for i in range(l):
            num = nums[i]
            total += num
            overallSum += num
            while total >= target:
                if (i - left + 1) < minlength:
                    minlength = i - left + 1
                total -= nums[left]
                left += 1
        if overallSum < target:
            return 0
        return minlength