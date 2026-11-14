class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        understand:
        input: list
        output: int

        plan:
        lets create a new list
        lets loop through tokens and check if its num;
        if num then add to the new list else
        join the last two elements of the new list using the operator and and pop the last element
        
        """
        newlist = []
        for i in range(len(tokens)):
            if tokens[i] not in set("+-*/"):
                newlist.append(int(tokens[i]))
                
            else:
                if tokens[i] == "+":
                    newlist[-2] = newlist[-2] + newlist[-1]
                if tokens[i] == "-":
                    newlist[-2] = newlist[-2] - newlist[-1]
                if tokens[i] == "*":
                    newlist[-2] = newlist[-2] * newlist[-1]
                if tokens[i] == "/":
                    newlist[-2] = int(newlist[-2] / newlist[-1])
                newlist.pop()
        return newlist[0]