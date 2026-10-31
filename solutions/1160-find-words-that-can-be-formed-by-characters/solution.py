class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        counts = Counter(chars)
        total = 0
        for word in words:
            include = True
            for c, count in Counter(word).items():
                if counts[c] < count:
                    include = False
                    break
            if include:
                total += len(word)
        return total
            