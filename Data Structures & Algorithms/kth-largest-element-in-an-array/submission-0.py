class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maintain min heap

        heap = []
        for i in nums:
            if len(heap) < k:
                heapq.heappush(heap, i)
            elif i > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
        
        return heapq.heappop(heap)
