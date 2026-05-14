class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num,0)

        heap = []

        # pushing into the heap (num , freq)

        for num in hashmap.keys():

            heapq.heappush(heap,(hashmap[num],num))

            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for ans in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        

        # hashmap = {}

        # for num in nums:
        #     if num in hashmap:
        #         hashmap[num] +=1
        #     else:
        #         hashmap[num] = 1
        
        # desc_order = dict(sorted(hashmap.items(),key=lambda x: x[1], reverse=True))

        # count = 0 
        # lst = []

        # for i in desc_order.keys():

        #     lst.append(i)
        #     count += 1
        #     if count == k:
        #         break

        # return lst
        