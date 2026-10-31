class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # gotta be BFS
        last = len(nums) - 1
        queue = deque()
        queue.append([0,0])
        added = set()
        added.add(0)
        while queue:
            i = queue.popleft()
            ind = i[0]
            val = nums[ind]
            numjumps = i[1]
            if ind == last:
                return numjumps
            j = ind
            while j <= ind + val:
                if j not in added:
                    queue.append([j, numjumps + 1])
                    added.add(j)
                j += 1
            