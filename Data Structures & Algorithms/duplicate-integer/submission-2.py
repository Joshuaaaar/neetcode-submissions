class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        
        sorted_array = sorted(nums)

        for i in range(len(nums)-1):

            if sorted_array[i] == sorted_array[i+1]:
                return True
        return False

        # for i1 in range(len(nums)):
        #     for i2 in range(i1 + 1, len(nums)):
        #         if nums[i1] == nums[i2]:
        #             return True
        # return False

                



        