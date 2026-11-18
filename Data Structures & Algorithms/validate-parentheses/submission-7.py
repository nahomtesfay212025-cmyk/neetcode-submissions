class Solution:
    def isValid(self, s: str) -> bool:
        """

        """
        if s[0] in "]})" or len(s) %2 != 0:
            return False
        new_dict = {"]":"[", ")":"(", "}":"{"}
        stack = []

        for ch in s:
            if ch in "({[":  # "([{}])"
                stack.append(ch)
            else:
                
                if stack:
                    if stack[-1] != new_dict.get(ch):
                        return False
                else:
                    return False
                stack.pop()
        return len(stack) == 0
        