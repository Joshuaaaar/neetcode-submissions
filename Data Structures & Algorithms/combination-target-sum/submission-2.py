class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        final_answer = []

        potential_sol = [] 

        n = len(nums)

        def backtracking(i, curr_sum):

            if curr_sum == target:
                final_answer.append(potential_sol[:])
                return
            
            if curr_sum > target or i == n:
                return

            backtracking(i+1, curr_sum)

            potential_sol.append(nums[i])

            backtracking(i, curr_sum + nums[i])

            potential_sol.pop()
        
        backtracking(0,0)

        return final_answer

            
            


                





        

        

        
        