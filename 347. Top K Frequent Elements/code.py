class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dd = defaultdict(int)
        for i in nums:
            dd[i]+=1
        heap = [(-value, key) for key, value in dd.items()]
        heapq.heapify(heap)
        L = []
        for _ in range(k):
            smallest = heapq.heappop(heap)
            L.append(smallest[1])
        return L