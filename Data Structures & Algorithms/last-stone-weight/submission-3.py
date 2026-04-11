class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heap
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)
        heapq.heapify(heap)

        while len(heap) > 1:
            l1 = -heapq.heappop(heap)
            l2 = -heapq.heappop(heap)
            if l1 != l2:
                heapq.heappush(heap, -(l1-l2))
            
        return -heapq.heappop(heap) if len(heap) == 1 else 0