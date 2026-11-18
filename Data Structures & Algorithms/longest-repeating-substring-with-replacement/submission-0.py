class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}

        left = 0
        max_val = 0
        longest = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1 # freq = {a;3, b;1}

            max_val = max(max_val,freq[s[right]] ) # len = right - left + 1 - 4
            while (right - left + 1) - max_val > k:
                freq[s[left]] -= 1
                left += 1
            
            longest = max(longest,right- left + 1 )
        return longest


