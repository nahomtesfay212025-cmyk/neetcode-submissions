class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        input:list, int k
        output:list

        plan:
        create dict of freq

        have two values to track max values
        nums[0]



        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0)+1

        ans = sorted(freq, key = freq.get, reverse = True)
        return ans[:k]