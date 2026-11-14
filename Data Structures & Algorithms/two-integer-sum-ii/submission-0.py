class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        understand:
        input: list and int
        output: list

        plan:
[3,5,8,9] target 8

        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

            


