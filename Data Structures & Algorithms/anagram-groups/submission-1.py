class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        understand:
        input: list
        output: list of lists

        plan:
        create a dictionary that maps sorted word with its anagram
        loop through the list
        key = sorted string item 
        value = real item 
        {act: [act, cat], ...}
        while creating the dictionary if the sorted item is not in the list create empty list 
        append it to new list

        finally return the values of the dictionary inside list
        """
        # implement:
        dct = {}
        for word in strs:
            val = "".join(sorted(word))
            if val not in dct:
                dct[val] = []
            dct[val].append(word)
        ans = []
        for val in dct.values():
            ans.append(val)
        return ans

        