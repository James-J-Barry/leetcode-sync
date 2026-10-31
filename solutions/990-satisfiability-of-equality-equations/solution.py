class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        parent = {}

        def find(x):
            parent.setdefault(x,x)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            parent[find(a)] = find(b)
        
        for eq in equations:
            if eq[1:3] == "==":
                union(eq[0], eq[3])
        for eq in equations:
            if eq[1:3] == "!=":
                if find(eq[0]) == find(eq[3]):
                    return False
        return True