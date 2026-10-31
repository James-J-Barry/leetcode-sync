class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result = [(nums[0], nums[0])]
        for i in range(1, len(nums)):
            last = result[-1]
            if last[1] == nums[i] - 1:
                result[-1] = (last[0], nums[i])
            else:
                result.append((nums[i], nums[i]))
        result = [f"{a}->{b}" if a != b else f"{a}" for (a,b) in result]
        return result
