class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        plan:
        initiate maxval, left and right
        while loop  
        if right is less than left move left 
        else move right

        """
        left = 0
        max_profit = 0
        for right in range(1, len(prices)):
            val = prices[right] - prices[left]
            max_profit = max(max_profit, val)
            
            while prices[left] > prices[right]:
                left += 1
        return max_profit

            
            
        