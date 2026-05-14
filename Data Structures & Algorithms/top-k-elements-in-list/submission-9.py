import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}

        for i in range(len(nums)):

            counter[nums[i]] = 1 + counter.get(nums[i],0)

        heap = []

        for key in counter.keys():

            heapq.heappush(heap, (counter[key],key))

            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for j in range(k):
            res.append(heapq.heappop(heap)[1])
        return res



