class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = [0]
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            current = temperatures[i]
            while stack and current > temperatures[stack[-1]]:
                ind = stack.pop()
                answer[ind] = i - ind
            stack.append(i)
        return answer
