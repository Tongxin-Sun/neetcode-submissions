class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            count[t] = count.get(t, 0) + 1
        
        time = 0
        q = deque()
        max_heap = []
        for k, v in count.items():
            heapq.heappush(max_heap, [-v, k])
        
        while max_heap or q:
            time += 1
            while q and q[0][2] == time:
                task, freq, t = q.popleft()
                heapq.heappush(max_heap, [freq, task])
            if max_heap:
                freq, task = heapq.heappop(max_heap)
                freq += 1
                if freq != 0:
                    q.append([task, freq, time + n + 1])
        return time