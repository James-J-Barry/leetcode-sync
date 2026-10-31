class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = len(s)
        dic = {}
        dic2 = {}
        for i in range(l):
            a = s[i]
            b = t[i]
            if (a in dic):
                if (dic[a] != b):
                    return False
            else:
                dic[a] = b
            if (b in dic2):
                if (dic2[b] != a):
                    return False
            else:
                dic2[b] = a
        return True