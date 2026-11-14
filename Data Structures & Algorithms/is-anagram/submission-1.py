class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        understand:
        input: two strings
        output: boolean
        edgecases: 



        """

        # if len(s) != len(t):
        #     return False
        
        return sorted(s) == sorted(t)
        