class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        order = []
        inDegrees = defaultdict(int)
        dependentOn = defaultdict(list)
        for a, b in prerequisites:
            inDegrees[a] += 1
            dependentOn[b].append(a)
        
        nextUp = deque([course for course in range(numCourses) if inDegrees[course] == 0])
        while nextUp:
            course = nextUp.popleft()
            order.append(course)
            for dep in dependentOn[course]:
                inDegrees[dep] -= 1
                if inDegrees[dep] == 0:
                    nextUp.append(dep)
                
        if len(order) != numCourses:
            return []
        return order

