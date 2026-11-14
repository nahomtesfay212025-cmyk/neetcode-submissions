class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        input: two strings
        output: boolean
        edgecases: if both strings donot have same length, both empty string 

        plan1:
        compare their sorted value and return true if they are same, otherwise false

        plan2:
        handle edgecase
        if len of both strings is not same then return false
        create frequency dictionary for both strings
        then loop through one of the dictionaries and compare its value with the other dictionaries value
        if they are not the same then return false
        after the loop ends return true
        """

        # implement1:
        return sorted(s) == sorted(t)

        # implement2:

        # if len(s) != len(t):
        #     return False
        # if len(s) == 0 and len(t) == 0:
        #     return True

        # freqs = {}
        # freqt = {}
        # for ch in s:
        #     freqs[ch] = freqs.get(ch, 0) + 1
        # for ch in t:
        #     freqt[ch] = freqt.get(ch, 0) + 1
        
        # for key, val in freqs.items():
        #     if val != freqt.get(key):
        #         return False
        # return True

        