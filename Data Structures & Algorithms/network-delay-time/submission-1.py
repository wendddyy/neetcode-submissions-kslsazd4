class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # sending node k must < all other senders
        # receiver node must contains all nodes from 1 to n 
        # for i in (1 to n): dfs(k, i)
        adj = collections.defaultdict(list)

        # build graph
        for u, v, w in times:
            adj[u].append((v, w))

        # shortest distance
        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        minHeap = [(0, k)]

        while minHeap:
            time, node = heapq.heappop(minHeap)

            # stale entry
            if time > dist[node]:
                continue

            for nei, w in adj[node]:
                new_time = time + w

                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(minHeap, (new_time, nei))

        ans = max(dist[1:])

        return ans if ans != float("inf") else -1