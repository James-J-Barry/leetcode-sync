class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = []
        maxn = nums[0]
        result = [0,0]
        for num in nums:
            while num - 1 >= len(counts):
                counts.append(0)
            counts[num - 1] += 1
        print(counts)
        for n in range(len(counts)):
            if counts[n] == 0:
                result[1] = n + 1
            elif counts[n] == 2:
                result[0] = n + 1
        if len(counts) < len(nums):
            result[1] = len(nums)
        return result


        
        
        
        # alln = 0
        # maxn = nums[0]
        # for num in nums:
        #     all = all ^ num
        #     if num > max:
        #         maxn = num
        # print(alln)
        # shouldbe = 0
        # for i in range(maxn):
        #     shouldbe += 

