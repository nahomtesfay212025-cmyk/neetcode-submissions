class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        plan:
        initiate shrink as zero
        initiate a max profit with tracks the maximum  diffrence betwen item in shrink and expand
        loop through the list using expand as index
        when prices[shrink] is greater than prices[expand] the condition fails 
        use start moving shrink forward

        update max_profit
        return the maximum profit

        implement:

        """
        shrink = 0
        max_profit = 0
        for expand in range(1,len(prices)):     # proces = [4,5,6,3,9]
            while prices[shrink] > prices[expand]:
                shrink += 1
            
            max_profit = max(max_profit, prices[expand] - prices[shrink])
        
        return max_profit
        