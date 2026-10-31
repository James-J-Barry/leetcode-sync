class Solution:
    def compress(self, chars: list[str]) -> int:
        current = chars[0]
        amt = 1
        result = ""
        for char in chars[1:]:
            if char == current:
                amt +=1
            else:
                result += current if amt == 1 else f"{current}{amt}"
                current = char
                amt = 1
        result += current if amt == 1 else f"{current}{amt}"
        chars[:] = list(result)
        return len(result)