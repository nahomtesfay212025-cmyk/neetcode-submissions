class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        understand:
        input: list, index-> day item-> price
        output: int_ the max profit  
        edgecase: if length of the list is 1

        match: sliding windows method with a variable size 
        plan: 
        if len of list is one then return 0
        lets initiate slow as 0
        max_val that updates the max profit
        use for loop to iterate the list from 1 to last index.
        comapre while item at fast is less than item from left
        if so increment left 
        update max_val

        return max_val

        implement:

        """
        if len(prices) == 1:
            return 0
        left = 0
        val = 0
        max_val = 0
        for right in range(1,len(prices)):
            while prices[right] < prices[left]:
                left += 1
            val = prices[right] - prices[left]
            max_val = max(max_val, val)

        return max_val



 
        
        