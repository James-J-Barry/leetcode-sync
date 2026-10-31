class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m, n = len(isConnected), len(isConnected[0])    
        parent = {}
        count = m

        def find(x):
            parent.setdefault(x, x)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b, count):
            if not find(a) == find(b):
                parent[find(a)] = find(b)
                return count - 1
            return count

        for i in range(m):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    count = union(i, j, count)

        return count