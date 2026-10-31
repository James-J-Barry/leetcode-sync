class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        for char in s:
            if char == '(':
                brackets.append('(')
            elif char == ')':
                if not brackets or brackets.pop() != '(':
                    return False
            elif char == '{':
                brackets.append('{')
            elif char == '}':
                if not brackets or brackets.pop() != '{':
                    return False
            elif char == '[':
                brackets.append('[')
            elif char == ']':
                if not brackets or brackets.pop() != '[':
                    return False
        return not brackets