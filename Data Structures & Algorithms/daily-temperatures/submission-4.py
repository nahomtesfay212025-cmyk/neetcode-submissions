class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        shrink
        expand  
        stack = [0]
        temperatures[expand] =temperatures[1] = 38
        stack[-1] = 0


        """
        stack = []
        ans = [0] * len(temperatures)
        
        
        for expand in range(len(temperatures)):
            
            while stack and temperatures[expand] > temperatures[stack[-1]]:
                indx = stack.pop()
                ans[indx] = expand - indx
            stack.append(expand)
        return ans
            

        
            

        