class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap

        heap = []

        def distance(x, y):
            return x*x + y*y

        for x, y in points:
            if len(heap) < k:
                heapq.heappush(heap, [-(distance(x, y)), x, y])
            elif -distance(x, y) > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, [-(distance(x, y)), x, y])

        return [[x, y] for dis, x, y in heap]