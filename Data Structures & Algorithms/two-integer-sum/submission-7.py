class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashS = {}
        # Populating hash map
        for i in range(len(nums)):
            hashS[nums[i]] = i 
        
        for i in range(len(nums)):

            y = target - nums[i]

            if y in hashS and hashS[y] != i:
                return [i,hashS[y]]


        
        