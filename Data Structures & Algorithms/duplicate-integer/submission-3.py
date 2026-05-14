class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:


        # o(n) time
        # o(n) space 

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False



        # o(nlogn) time 
        # o(1) space 
        
        # sorted_array = sorted(nums)

        # for i in range(len(nums)-1):

        #     if sorted_array[i] == sorted_array[i+1]:
        #         return True
        # return False


        # o(n^2) time
        # o(1) space

        # for i1 in range(len(nums)):
        #     for i2 in range(i1 + 1, len(nums)):
        #         if nums[i1] == nums[i2]:
        #             return True
        # return False

                



        