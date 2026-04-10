class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # find turning point
        # stack store index
        res = [0] * len(temperatures)
        stack = deque()
        if not temperatures:
            return res

        stack.append(0)
        for cur in range(len(temperatures)):
            while stack and temperatures[cur] > temperatures[stack[-1]]:
                res[stack[-1]] = cur - stack[-1]
                stack.pop()
            stack.append(cur)
        
        return res

        

        