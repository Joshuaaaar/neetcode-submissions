class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # optimal solution with hashmap

        # value: index 
        hash_map = {} 

        for i , value in enumerate(nums):
            diff = target - value
            if diff in hash_map:
                return [hash_map[diff],i]
            hash_map[value] = i
        
    
        # o(n^2) time complexity
        # o(1) memory 
        # for i in range(len(nums)):

        #     for j in range(i+1,len(nums)):

        #         if (nums[i] + nums[j]) == target:

        #             return [i,j]
        
        