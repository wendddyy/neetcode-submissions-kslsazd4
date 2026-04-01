class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # step1: count frenq for each num
        freq = Counter(nums)


        # step2: put them into a min_heap of len(k)
        min_heap = []
        for number, frequency in freq.items():
            heapq.heappush(min_heap, (frequency, number))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # step3: pop them into a result list
        result = []
        while min_heap:
            frequency, number = heapq.heappop(min_heap)
            result.append(number)

        return result
        