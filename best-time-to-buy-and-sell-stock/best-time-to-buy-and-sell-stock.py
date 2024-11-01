class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_stock_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_stock_price:
                min_stock_price = min(min_stock_price, price)
            max_profit = max(max_profit, price - min_stock_price)

        return max_profit