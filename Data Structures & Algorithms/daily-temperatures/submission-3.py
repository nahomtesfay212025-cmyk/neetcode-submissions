class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        [1,2,3,4]
        s = [0]
        ans[0] = 
        """
        ans = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                indx = stack.pop()
                ans[indx] = i - indx

            stack.append(i)
        return ans

        

        
         
        