class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        m, n = len(s1), len(s2)
        # corner
        if n < m:
            return False

        # init source of truth
        win = [0] * 26
        source = [0] * 26
        for char in s1:
            source[ord(char) - 97] += 1

        # init window
        for i in range(m):
            win[ord(s2[i]) - 97] += 1
        if win == source:
            return True

        # start sliding
        for right in range(m, n):
            win[ord(s2[right]) - 97] += 1
            win[ord(s2[right - m]) - 97] -= 1
            if win == source:
                return True
        
        return False