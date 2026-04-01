class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[n] = cost[n-1] + dp[n-1] or cost[n-2] + dp[n-2]

        prev1, prev2 = 0, 0
        cur = 0
        for i in range(2, len(cost) + 1):
            cur = min(prev1 + cost[i-1], prev2 + cost[i-2])
            prev2 = prev1
            prev1 = cur
        
        return cur