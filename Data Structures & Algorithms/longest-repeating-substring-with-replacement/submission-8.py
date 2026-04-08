class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        slow, fast = 0, 0
        freq = {} # int - freq
        maxFreq = 0
        res = 0

        while fast < len(s):
            freq[s[fast]] = 1 + freq.get(s[fast], 0)
            maxFreq = max(maxFreq, freq[s[fast]])

            while (fast - slow + 1) - maxFreq > k:
                freq[s[slow]] -= 1
                slow += 1
            res = max(res, fast - slow + 1)
            fast += 1
        
        return res
                