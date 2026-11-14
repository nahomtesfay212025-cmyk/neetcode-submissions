class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        input: list and output integer

        nums = [3,4,5,6,1,2] 
        """
       
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
        