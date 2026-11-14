class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch not in "+-*/": # [9,4]
                stack.append(int(ch))
            elif ch == "+":
                stack[-2] = stack[-1] + stack[-2]
                stack.pop()
            elif ch == "-":
                stack[-2] = stack[-2] - stack[-1]
                stack.pop()
            elif ch == "*":
                stack[-2] = stack[-1] * stack[-2]
                stack.pop()
            else:
                stack[-2] = int(stack[-2] /stack[-1])
                stack.pop()
        return stack[0]

