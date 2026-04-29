class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        
        heap = [(-cnt, task) for task, cnt in freq.items()]
        heapq.heapify(heap)

        cooldown = deque()

        time = 0

        while heap or cooldown:
            time += 1
            if heap:
                cnt, task = heapq.heappop(heap)
                cnt += 1
                if cnt < 0:
                    cooldown.append((time+n, cnt, task))

            if cooldown and cooldown[0][0] == time:
                _, cnt, task = cooldown.popleft()
                heapq.heappush(heap, (cnt, task))

        return time
