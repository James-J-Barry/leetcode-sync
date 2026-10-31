class Solution:
    def isHappy(self, n: int) -> bool:
        ndict = {}
        def process(num, ndict):
            if num in ndict:
                return ndict[num]
            else:
                result = sum([int(i) ** 2 for i in list(str(num))])
                ndict[num] = result
                return result
            
        slow = n
        fast = n
        while slow != 1 and fast != 1:
            slow = process(slow, ndict)
            fast = process(process(fast, ndict), ndict)
            if slow != 1 and fast != 1 and slow == fast:
                return False
        return True
