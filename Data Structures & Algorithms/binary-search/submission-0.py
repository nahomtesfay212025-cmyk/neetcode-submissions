class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        lets use binary search for o(logn)
        understand:
        input: list
        output: int

        plan:
        lets get mid that is an average of left and right
        then we need prev val 



        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = right + left // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            
        return -1
        