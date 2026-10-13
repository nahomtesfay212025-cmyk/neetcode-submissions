class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        understand:
        input: list
        output: int

        plan:
       lets uses bineary search tree 
       initiate left as 0 and right last index
       use while loop when left is less than right
      

        """
        left = 0
        right = len(numbers) - 1
        while left <= right:
            total = numbers[left] + numbers[right]
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1