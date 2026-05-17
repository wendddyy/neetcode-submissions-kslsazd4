class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        have = 0
        freq = Counter(t)
        visited = {}

        res = [-1, -1]
        res_len = float('inf')

        left = 0
        for right in range(len(s)):
            c = s[right]
            visited[c] = visited.get(c, 0) + 1
            if c in freq and visited[c] == freq[c]:
                have += 1
            
            while have == len(freq):
                left_c = s[left]
                visited[left_c] -= 1

                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res = [left, right]
                
                if left_c in freq and visited[left_c] < freq[left_c]:
                    have -= 1
                left += 1
        
        l, r = res
        return s[l : r + 1] if res_len != float('inf') else ""
