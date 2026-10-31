class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        vals = {}
        for i in range(len(nums)):
            num = nums[i]
            needed = target - num
            if needed in vals:
                return [i, vals[needed]]
            vals[num] = i