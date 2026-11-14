class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        understand:
        input: array
        output: integer 
        edge cases: 

        match:
            two pointers

        plan:
        intialize the pointers
        left as zero and right as the last index
        initiate area as zero
        use while loop until left is not less than right
        find the area at the pointers and compare it the prev area 
        if the computed area is greater than the prev one then assign the prev one to be the computed area.
        return area
        """
        left = 0
        right = len(heights) - 1
        max_area = 0
        # area = 0

        while left < right:
            width = right - left
            length = min(heights[left], heights[right]) 
            area = width * length
            if area > max_area:
                max_area = area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area


       