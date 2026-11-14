class Solution:
    def isValid(self, s: str) -> bool:
        """
        plan:
        create an empty stack list -> stack = []
        edgecase: if the first item is ")}]" then return false
        if length of the string is odd then return false
        create a dict that maps closing with opening



        s = "([{}])"
        loop through the str
        append to the stack

        if item(s[i]) is closing compare the values with its respective dictionary
        if not the same then return false

        if they are same, pop the top element

        leave the loop and return true


        stack = ["(","[","{"]


        """
        if s[0] in "}])" or len(s) %2 != 0:
            return False

        map_dict = {")":"(", "]":"[", "}":"{"}

        stack = []
        for ch in s:
            if ch in "({[":  # s="(){}}{"    stack = []
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack and stack[-1] != map_dict[ch]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
        
                

            



        
        