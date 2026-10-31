class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        #intuition -> tasks do not have to be completed in order, I need a count of how many of each label
        counts = Counter(tasks)
        maxCountL = max(counts.values())
        n_max = sum(1 for c in counts.values() if c == maxCountL)
        return max(len(tasks), (maxCountL - 1) * (n + 1) + n_max)
        
        
