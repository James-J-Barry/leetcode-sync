class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = deque()
        for tok in tokens:
            if tok == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif tok == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif tok == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif tok == "/":
                a = stack.pop()
                b = stack.pop()
                print(str(b) + "/" + str(a))
                stack.append(math.trunc(b / (a+0.0)))
            else:
                stack.append(int(tok))
        return stack.pop()
        