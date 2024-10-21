class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted((float(w) / q, q) for q, w in zip(quality, wage))
        res = float('inf')
        qsum = 0
        heap = []
        
        for ratio, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > k:
                qsum += heapq.heappop(heap)
            if len(heap) == k:
                res = min(res, ratio * qsum)
        
        return res