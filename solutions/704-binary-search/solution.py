class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = int((lo + hi)/2)
            print(f"{lo}, {hi}, {mid}")
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return -1