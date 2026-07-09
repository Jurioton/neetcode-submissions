class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_value = prices[0]

        for i in prices:
            if i < min_value:
                min_value = i
            profit = i - min_value
            if profit > max_profit:
                max_profit = profit
        return max_profit



        
        

        