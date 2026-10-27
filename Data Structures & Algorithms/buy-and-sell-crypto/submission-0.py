class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        input: list
        output: integer

        plan:

        """
        buy = 0
        maxval = 0
        for sell in range(len(prices)):
            if prices[sell] > prices[buy]:
                maxval = max(maxval, prices[sell]-prices[buy])

            else: 
                buy = sell
            
        return maxval

        
        