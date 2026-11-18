class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            elif token == "+":
                stack[-2] = stack[-2] + stack[-1]
                stack.pop()
            elif token == "-":
                stack[-2] = stack[-2] - stack[-1]
                stack.pop()
            elif token == "*":
                stack[-2] = stack[-2] * stack[-1]
                stack.pop()
            else:
                stack[-2] = int(stack[-2] / stack[-1])
                stack.pop()
        return stack[0]

        