class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {1:1,2:2}

        def fib(n):

            if n not in memo:
                memo[n] = fib(n-1) + fib(n-2)
            
            else:
                return memo[n]
        
        return fib(n)

