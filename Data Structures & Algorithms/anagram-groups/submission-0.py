class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        understand:
        input: list
        output: list

        plan:
        create an empty dict
        iterate through the list
        key - item of list
        value - if the items are anagram to the key then append it 


        """

        

        # if len(strs[0]) == 0:
        #     return [[""]] 

        newdict = {}

        for i in range(len(strs)):
            word = strs[i]
            sorti = sorted(word)
            sorte = "".join(sorti)       
            if sorte not in newdict:
                newdict[sorte] = []

            
            newdict[sorte].append(word)
        

        # ans = []
            
        # for value in newdict.values():
        #     ans.append(value)
        return list(newdict.values())

        