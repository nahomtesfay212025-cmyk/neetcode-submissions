class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        input: list
        output: boolean

        plan1:
        (less optimized) time complexity: O(n), space complexity: O(n)

        create a freq dict 
        iterate through the dictionary and return true if value is greater than 1
        after the loop ends return false

        plan2:

        time complexity = O(n), space complexity = O(n)

        create an empty dict 
        loop through the given list
        check if the number is not on the dictionary
        if so add it 
        else return true 
        finish the loop end return false


        """

        # implemnt1:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for val in freq.values():
            if val > 1:
                return True
        return False

        # implement2:
        # freq = {}
        # for num in nums:
        #     if num not in freq:
        #         freq[num] = 1
        #     else:
        #         return True
        # return False








        