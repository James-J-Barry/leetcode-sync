class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        def runthrough(start, l, gas, cost):
            tank = 0
            current = start
            while True:
                tank += gas[current]
                tank -= cost[current]
                if tank >= 0:
                    current += 1
                    current = current % l
                else:
                    return [False, current]
                if current == start:
                    return [True, current]
        l = len(gas)
        nextviable = 0
        while True:
            ret = runthrough(nextviable, l, gas, cost)
            if ret[0]:
                return ret[1]
            else:
                nextviable = ret[1] + 1
        
        
        # l = len(gas)
        # for i in range(l):
        #     if (gas[i] - cost[i]) > 0 or l == 1:
        #         if runthrough(i, l, gas, cost):
        #             return i
        # return -1

        # temp = []
        # for i in range(len(gas)):
        #     temp.append(gas[i] - cost[i])
        # print(temp)
        