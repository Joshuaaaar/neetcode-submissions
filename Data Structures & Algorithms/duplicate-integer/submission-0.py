class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        
        for i1 in range(len(nums)):
            for i2 in range(i1 + 1, len(nums)):
                if nums[i1] == nums[i2]:
                    return True
        return False

                



        