class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        create a freq dict
        {1:1, 2:2, 3:3} , k = 2
        then sort it based on it frequency
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0)+1

        ans = sorted(freq, key=freq.get, reverse = True)

        return ans[:k]
        
        
        