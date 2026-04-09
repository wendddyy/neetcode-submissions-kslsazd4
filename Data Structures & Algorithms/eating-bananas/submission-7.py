class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        if h == len(piles):
            return max(piles)
        
        def eatingTime(k):
            hours = 0
            for i in piles:
                hours += (i + k - 1) // k
            return hours

        while left <= right:
            mid = (left + right) // 2
            if eatingTime(mid) > h:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
