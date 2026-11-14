class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        understand:
        input: string
        output: boolean

        match:
            two pointers
        
        plan:
        we need create a new empty string 
        loop through the string and add if they are num or alpha
        then initiate two pointers left as 0 and right as the last index
        use while loop until left is not less than right and 
        have a condition that compares left with right item and if they not same return false

        return true


        """
        ans = ""
        for ch in s:
            if ch.isalnum():
                ans += ch.lower()
        left = 0
        right =len(ans) - 1
        while left < right:
            if ans[left] != ans[right]:
                return False
            
            left += 1
            right -= 1
        return True
        

