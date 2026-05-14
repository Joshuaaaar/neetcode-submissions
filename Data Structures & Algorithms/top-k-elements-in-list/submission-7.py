import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        h = {}

        for i in range(len(nums)):

            h[nums[i]] = 1 + h.get(nums[i],0)
        
        heap = []

        for num in h.keys():
            heapq.heappush(heap, (h[num],num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        


