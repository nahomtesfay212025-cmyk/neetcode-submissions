class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        input: string 
        output: integer

        plan:
        initiate left and maxlen as 0
        create empty list with first item of s in it
        then loop right for string s
        check while right in new list 
            if not then add it to the list and update maxval
        else: 
            add it and remove the first item

        return maxlen

        """

        left = 0
        maxlen = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            maxlen = max(maxlen, len(seen))



        return maxlen
