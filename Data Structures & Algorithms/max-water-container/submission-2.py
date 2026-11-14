class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        input: array , item - height , index = width
        output: integer , maximum amount of water
        # edgecases: if length of the list is less than two

        plan:
        two pointers
        initiate left and right
        initiate max_area as zero
        use a while loop until left is greater than right
        area = difference in index times minimum hight of the two items
        compare area with max area and if its greater than update it
        increment and decrement left and right

        outside the loop return max_area

        implement:

        """
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(heights[right], heights[left])
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            if area > max_area:
                max_area = area
            
        
        return max_area
        