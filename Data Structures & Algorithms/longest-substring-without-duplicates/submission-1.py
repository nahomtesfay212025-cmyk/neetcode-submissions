class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_val = 0
        d = {}
        left = 0

        for right in range(len(s)):
            

            while s[right] in d:       # s[right] = z  left = 0, right = 3
                if d[s[right]] == 1:
                    del d[s[left]]
                else:
                    d[s[left]] -= 1
                left += 1
            
            d[s[right]] = d.get(s[right], 0)+1 # d = {z;1,  x:1, y:1}
            max_val = max(max_val, right - left + 1)
        return max_val
                
           
        
       



      





        