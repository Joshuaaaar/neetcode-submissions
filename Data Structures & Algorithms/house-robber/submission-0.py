class Solution:
    def rob(self, nums: List[int]) -> int:

        curr1 = 0
        curr2 = 0

        counter = 0

        i = 0
        j = 1

        while counter < len(nums):

            if i < len(nums):
                curr1 += nums[i]
                i +=2

            if j < len(nums):
                curr2 += nums[j]
                j +=2
    
            counter +=1 
        
        if curr1 > curr2:

            return curr1

        else:

            return curr2

