class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        product = 1 
        for n1 in range(len(nums)):

            for n2 in range(len(nums)):
                
                if n1 == n2:
                    # do nothing
                    continue

                product *= nums[n2]
            
            res.append(product)
            product = 1
        
        return res
         
        