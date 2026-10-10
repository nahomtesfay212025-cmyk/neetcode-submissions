class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        understand:
        input: list of nums, int target
        output: list of indices

        plan:
        lets use nested for loop 
        

        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        