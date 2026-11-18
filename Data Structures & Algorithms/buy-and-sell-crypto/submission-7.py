class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        shrink = 0
        max_val = 0
        for expand in range(1,len(prices)):
            while prices[shrink] > prices[expand]:
                shrink += 1
            max_val = max(max_val, prices[expand] - prices[shrink])
        return max_val

            

        