class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        understand:
        input: list

        edgecases: empty list

        plan:
        create empty dictionary;
        get freq dict 
        iterate through the dict and if val is greater 1 then return true 
        else false



        """
        freq = {}
        if len(nums) == 0:
            return False
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for val in freq.values():
            if val > 1:
                return True
        return False
        