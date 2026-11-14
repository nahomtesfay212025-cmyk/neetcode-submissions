class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        UMPI method:
        understand:
        input: two strs
        output: boolean
        edgecases: 


        """
        dic = {}
        mic = {}
        for x in s:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
        for y in t:
            if y in mic:
                mic[y] += 1
            else:
                mic[y] = 1
        if dic == mic:
            return True
        else:
            return False               
