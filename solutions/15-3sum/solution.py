class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        for i in range(len(nums)):
            if i != 0:
                if nums[i] == nums[i - 1]:
                    continue
            a = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = a + nums[j] + nums[k]
                if sum == 0:
                    results.append([a, nums[j], nums[k]])

                    while j < k and nums[j + 1] == nums[j]:
                        j += 1
                    while j < k and nums[k - 1] == nums[k]:
                        k -= 1

                    j += 1
                    k -= 1

                elif sum < 0:
                    j = j + 1
                else:
                    k = k - 1
        return results

        