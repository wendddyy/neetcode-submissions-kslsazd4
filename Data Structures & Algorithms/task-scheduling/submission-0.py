class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxfreq = max(freq.values())
        countMax = sum(1 for v in freq.values() if v == maxfreq)

        return max(len(tasks), (n+1)*(maxfreq-1)+countMax)