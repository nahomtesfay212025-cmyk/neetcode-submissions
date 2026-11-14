class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        understand:
        input: string -> list of characters
        output: integer -> length of longest substring without duplicate
        edgecases: empty string 



        plan:
        lets use variable size sliding windows method
        lets have two pointers shrink and expand
        create an empty set called seen
        intialize longest size variabe, long_val = 0

        lets iterate through the string (use expand as index)
        add expand to seen 
        if item in seen -> by item we mean s[expand]
        start shrinking by removing from left -> remove left item from seen
        increment shrink

        update long_val -> subtract shrink from expand
        return long_val

        implement:

        """
        shrink = 0
        seen = set()
        long_val = 0
        for expand in range(len(s)):
            
            while s[expand] in seen: 
                seen.remove(s[shrink])
                shrink += 1
            seen.add(s[expand])
            long_val = max(long_val, expand - shrink + 1)
        return long_val








        