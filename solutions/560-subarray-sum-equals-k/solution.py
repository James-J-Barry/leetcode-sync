class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        result = 0
        currentSum = 0
        for num in nums:
            currentSum += num
            lookingFor = currentSum - k
            result += prefixSum[lookingFor]
            prefixSum[currentSum] += 1
        return result
        
        
        
        
        
        
        
        
        # currentSum = 0
        # prefixSum = []
        # for num in nums:
        #     currentSum += num
        #     prefixSum.append(currentSum)
        
        # counts = Counter(prefixSum)
        # print(counts)
        # result = 0
        # for num in prefixSum:
        #     #k = num - p
        #     lookingFor = num - k
        #     print(f"{num}, {lookingFor}")
        #     result += counts[lookingFor]
        # return result

        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums) + 1):
        #         theSum = sum(nums[i:j])
        #         if theSum == k:
        #             count += 1
        # return count

        # [1, 3, 6]


        
        
        
        # i = 0
        # j = 1
        # l = len(nums)
        # # s[i,j]
        # currentSum = nums[0]
        # while i < j and j < l:
        #     currentSum += nums[j]
        #     if currentSum < k