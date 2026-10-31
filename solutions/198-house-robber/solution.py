class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxat = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            print(maxat)
            maxat.append(max(maxat[i-1], maxat[i-2] + nums[i]))
        return maxat[-1]