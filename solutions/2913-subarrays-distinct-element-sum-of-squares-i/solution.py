class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums) + 1):
                count = len(set(nums[i:j]))
                result += count ** 2
        return result
