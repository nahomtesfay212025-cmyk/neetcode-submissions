class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        understand:
        input: string s and t
        output: bool

        plan:
        compare the len of both str and if not same 
        return false
        create freq dict for both 
        then iterate through s and if they have not same val then return false

        """
        if len(s) != len(t):
            return False
        
        freq1 = {}
        freq2 = {}
        for ch in s:
            freq1[ch] = freq1.get(ch, 0) + 1
        for ch in t:
            freq2[ch] = freq2.get(ch, 0) + 1
        for key, val in freq1.items():
            if val != freq2.get(key,0):
                return False
        return True

        