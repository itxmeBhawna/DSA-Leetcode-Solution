class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        max_profit = 0
        for i in prices:
            if i < min_buy:
                min_buy = i
            profit = i - min_buy
            if profit > max_profit:
                max_profit = profit
        return max_profit        


        