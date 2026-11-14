class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        understand:
        input: array
        output: boolean
        edgecases: empty list

        match:
            dict

        plan:
        if length of the list is 0 then return false
        create an freq dict 
        iterate through the dict and check if value is greater than one
        if so then return true 

        return false

        complexity: 
        space comp = O(n)
        time comp = 0(n)
        
        implement:

        """

        if len(nums) == 0:
            return False
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
            # freq[num] = get.freq(num, 0) + 1

        for value in freq.values():
            if value > 1:
                return True
        return False

        
        
        