class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        understand:
        input: list of strings
        output: list of lists

        plan:
        create an empty dict 
         key of string maps with its anagram words 
         return list of values from the dictionary


        """
        newdict = {}
        newlist = []
        for s in strs:
            t = "".join(sorted(s))

            if t not in newdict:
                newdict[t] = [s]
            else:
                newdict[t].append(s)

        answer = []
        for val in newdict.values():
            answer.append(val)
        return answer
