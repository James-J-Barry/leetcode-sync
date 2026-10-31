class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        def helper(graph, node, visited):
            if node in visited:
                return visited[node]
            if node == len(graph) - 1:
                return [[len(graph) - 1]]
            totalPaths = []
            for edge in graph[node]:
                edgePaths = helper(graph, edge, visited)
                for path in edgePaths:
                    totalPaths.append([node] + path)
            visited[node] = totalPaths
            return totalPaths
        visited = dict()
        return helper(graph, 0, visited)