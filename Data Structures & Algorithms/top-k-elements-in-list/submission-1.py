class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        understand:
        input: list of numbers and int of k
        output: list of the k most frequent elements

        plan:
        create an freq dict
        then sorted it based on freq which is values and return key up to k
        """

        # implement:
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        ans = sorted(freq, key = freq.get, reverse = True)
        return ans[:k]
        