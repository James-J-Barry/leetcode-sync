class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        ndict = {}
        for i in range(len(nums)):
            if nums[i] in ndict:
                if i - ndict[nums[i]] <= k:
                    return True
                ndict[nums[i]] = i
            else:
                ndict[nums[i]] = i
        return False
        
