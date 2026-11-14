class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        understand:
        input: list of nums and int of target
        output: list of two indices that sumup the terget value

        match:


        plan1:(least optimal because O(n) = n^2, space comlexity is O(1))
        use nested for loop
        check if they sum up to the target if so return their indices 

        plan2:
        create a dictionary that maps number(key) with its index(val)

        so loop through nums and subtract target with item in the list and look for it in dict 
        if found then return both indices
        else add the item to the dict

        plan3: if sorted:
        use two pointers and move them based on a condition

        
        """

        # implement1:
        # ans = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # implement2:
        dct = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in dct:
                return [dct[val],i]
            else:
                dct[nums[i]] = i

        # implement3:
        # left = 0
        # right = len(nums) - 1
        # while left < right:
        #     if nums[left] + nums[right] == target:
        #         return [left,right]
        #     elif nums[left] + nums[right] > target:
        #         right -= 1
        #     else:
        #         left += 1
            


        