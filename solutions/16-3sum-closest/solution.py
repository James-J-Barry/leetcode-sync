class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]  # initialize with first triplet

        for i in range(n - 2):
            j, k = i + 1, n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                # update closest if this sum is better
                if abs(total - target) < abs(closest - target):
                    closest = total

                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    return total  # exact match found

        return closest
