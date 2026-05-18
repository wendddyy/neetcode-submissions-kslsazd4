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
            source[ord(char) - ord('a')] += 1

        # start sliding
        left = 0
        for right in range(n):
            win[ord(s2[right]) - ord('a')] += 1
            if right - left + 1 > m:
                win[ord(s2[left]) - ord('a')] -= 1
                left += 1
            if win == source:
                return True
        
        return False