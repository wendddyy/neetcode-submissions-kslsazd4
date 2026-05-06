class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maintain left/right bound
        # when update left? right < left
        # when update right? no need to manually update, ues it to iterate

        #corner 
        if len(prices) == 1:
            return 0

        max_profit = 0
        left = 0

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                max_profit = max(max_profit, prices[right] - prices[left])
                
        return max_profit