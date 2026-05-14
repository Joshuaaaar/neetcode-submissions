class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        l = 0
        for i in range(len(prices) - 1):
            r = i + 1
            if prices[r] - prices[l] < 0:
                l = r 
            else:
                profit = prices[r] - prices[l]
                if profit > max_profit:
                    max_profit = profit
        return max_profit
            

            


        