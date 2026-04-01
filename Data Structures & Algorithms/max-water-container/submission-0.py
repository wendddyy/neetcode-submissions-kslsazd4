class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers + max(cur_max, width * height)
        res = 0
        for i in range(len(heights) - 1):
            for j in range(i+1, len(heights)):
                width = j - i
                height = min(heights[i], heights[j])
                res = max(res, width * height)
        
        return res