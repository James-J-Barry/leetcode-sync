class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        result = sorted(list(counts.keys()), key=lambda iv: counts[iv])[-k:]
        return result

                