class Solution:
    def isValid(self, s: str) -> bool:
        # use stack
        p_map = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = deque()
        for i in range(len(s)):
            if s[i] in p_map:
                if not stack or p_map[s[i]] != stack.pop():
                    return False
            else:
                stack.append(s[i])
        return not stack