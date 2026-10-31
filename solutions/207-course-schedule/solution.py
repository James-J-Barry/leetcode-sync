class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        #topo sort
        inDegrees = defaultdict(int)
        dependantOn = defaultdict(list)
        for prerec, course in prerequisites:
            inDegrees[course] += 1
            dependantOn[prerec].append(course)
        remainingCourses = set(range(numCourses))
        toRemove = [course for course in remainingCourses if inDegrees[course] == 0]
        while toRemove:
            for course in toRemove:
                remainingCourses.remove(course)
                toRemove.remove(course)
                for dep in dependantOn[course]:
                    inDegrees[dep] -= 1
                    if inDegrees[dep] == 0:
                        toRemove.append(dep)
        if remainingCourses:
            return False
        return True

