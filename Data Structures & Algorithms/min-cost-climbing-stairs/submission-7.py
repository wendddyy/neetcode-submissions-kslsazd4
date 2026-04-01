class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[n] = cost[n-1] + dp[n-1] or cost[n-2] + dp[n-2]

        # corner
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])

        dp = [0] * (len(cost)+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[len(cost)]