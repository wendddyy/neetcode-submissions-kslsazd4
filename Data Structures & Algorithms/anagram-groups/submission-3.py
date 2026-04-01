class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            presence = [0] * 26
            for l in s:
                presence[ord(l) - ord('a')] += 1
            res[tuple(presence)].append(s)
        return list(res.values())
        