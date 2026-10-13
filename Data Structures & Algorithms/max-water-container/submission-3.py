class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        understand:
        input: list
        output: integer
        height = value of list(item of list)
        width = index
        area = width * height

        match:
            two pointer
        plan:
        initiate left and right as first and last index
        then create max as 0
        while loop when left is less than right
        find the area
        if right is greater than left
        and increment left
        else decrement right
        update max value
        return max value
        """
        left = 0
        right = len(heights) - 1
        area = 0
        max_area = 0
        while left <= right:
            area = min(heights[right], heights[left]) * (right-left)
            max_area = max(max_area, area)
            if heights[right] >= heights[left]:
                left += 1
            else :
                right -= 1

        return max_area