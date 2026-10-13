class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        input: string
        output: bool

        plan:
        lets create a string
        loop through s and add it to new str if its alnum 
        when adding it change the ch to its lower case
        return new string comparing with its reverse

        """
        new = ""
        for ch in s:
            if ch.isalnum():
                new += ch.lower()
        return new == new[::-1]