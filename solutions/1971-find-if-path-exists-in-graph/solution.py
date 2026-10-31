class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        #construct adjacency list:
        connections = defaultdict(set)
        for u, v in edges:
            connections[u].add(v)
            connections[v].add(u)
        #BFS
        queue = deque([source])
        visited = set([source])
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for c in connections[node]:
                if not c in visited:
                    queue.append(c)
                    visited.add(c)
        return False