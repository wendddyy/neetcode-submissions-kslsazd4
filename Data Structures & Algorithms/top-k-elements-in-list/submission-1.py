class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # min heap
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        heap = []
        for c in count.keys():
            heapq.heappush(heap, (count[c], c))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        
        