class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] +=1
            else:
                hashmap[num] = 1
        
        desc_order = dict(sorted(hashmap.items(),key=lambda x: x[1], reverse=True))

        count = 0 
        lst = []

        for i in desc_order.keys():

            lst.append(i)
            count += 1
            if count == k:
                break

        return lst
        