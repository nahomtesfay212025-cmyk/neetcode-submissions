class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        understand:
        input: list
        output: int
        match:
            sliding window method

        plan:
        lets sort the list
        lets create val = 0
        # lets create empty slid window list
        and max value with 0

        use while loop 
        comapre left and right then add one to the val and keep updating the max val
        else make val 0 and restart again
        return max val
        """

        if len(nums) == 0:
            return 0
        sorted_list = sorted(nums)

        val = 1
        max_val = 1
        left = 0 
        right = 1
      
        while right < len(sorted_list):
            if sorted_list[right] - sorted_list[left] == 1:
                val += 1
                max_val = max(max_val, val)
            elif sorted_list[right] - sorted_list[left] == 0:
                pass
            else:
                val = 1
            left += 1
            right += 1
        
        return max_val



        