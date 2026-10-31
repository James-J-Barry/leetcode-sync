class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        # brute force: BFS from each node
        answer = [[] for _ in range(n)]
        decendants = defaultdict(list)
        for fromNode, toNode in edges:
            decendants[fromNode].append(toNode)

        for node in range(n):
            queue = deque(decendants[node])
            visited = set(decendants[node])
            while queue:
                toVisit = queue.popleft()
                answer[toVisit].append(node)
                for nod in decendants[toVisit]:
                    if not nod in visited:
                        visited.add(nod)
                        queue.append(nod)
    
        return answer





        # find no ancestor nodes
        # inDegree = defaultdict(int)
        # decendants = defaultdict(list)
        # for fromNode, toNode in edges:
        #     inDegree[toNode] += 1
        #     decendants[fromNode].append(toNode)
        # noAncestors = [node for node in range(n) if inDegree[node] == 0]
        # answer = [[] for _ in range(n)]
        # def dfsHelper(node, ancestors):
        #     #answer starts sorted
        #     for anc in ancestors:
        #         if not anc in answer[node]:
        #             bisect.insort(answer[node], anc)
        #     for child in decendants[node]:
        #         dfsHelper(child, ancestors + [node])
        
        # for node in noAncestors:
        #     dfsHelper(node, [])

        # return answer




        
        
