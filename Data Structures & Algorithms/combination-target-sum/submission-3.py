class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)

        res = []
        solu = []

        def backtrack(i, curr_sum):

            if curr_sum == target:
                res.append(solu[:])
                return
            
            if curr_sum > target or i == n:
                return
            

            backtrack(i+1, curr_sum)

            solu.append(nums[i])

            backtrack(i, curr_sum + nums[i])

            solu.pop()

        backtrack(0,0)

        return res



            
            


                





        

        

        
        