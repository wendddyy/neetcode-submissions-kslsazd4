class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        hold = -prices[0]
        rest = 0
        sold = float('-inf')

        for p in prices[1 :]:
            prev_hold = hold
            prev_rest = rest
            prev_sold = sold

            hold = max(prev_hold, prev_rest - p)
            rest = max(prev_rest, prev_sold)
            sold = prev_hold + p

        return max(rest, sold)