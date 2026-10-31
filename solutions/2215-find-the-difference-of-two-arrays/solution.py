class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1 = set()
        for num in nums1:
            set1.add(num)
        set2 = set()
        for num in nums2:
            set2.add(num)
        answer = [0,0]
        answer[0] = list(set1.difference(set2))
        answer[1] = list(set2.difference(set1))
        return answer