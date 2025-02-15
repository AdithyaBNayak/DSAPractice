class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_value = float("inf")

        for price in prices:
            profit = max(profit,price-min_value)
            min_value = min(price,min_value)
            
            # if price < min_value:
            #     min_value = price
            # elif price - min_value > profit:
            #     profit = price - min_value
        return profit        
