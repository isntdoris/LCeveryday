class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for time in times:
            graph[time[0]].append([time[1], time[2]])

        minHeap = [(0, k)]
        shortest = {}
        while minHeap:
            w1, n1 = heapq.heappop(minHeap) # RICKY HERE: minHeap得把要比大小的東西放在前面
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in graph[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return max(shortest.values()) if len(shortest) == n else -1