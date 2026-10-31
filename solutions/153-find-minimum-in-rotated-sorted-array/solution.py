class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            print(f"lo: {nums[lo]}, mid: {nums[mid]}, hi: {nums[hi]}")
            if nums[mid] > nums[hi]:
                lo = mid + 1
                print(f"hi: {hi}")
            else:
                hi = mid 
                print(f"lo: {lo}")
        return nums[lo]
        
