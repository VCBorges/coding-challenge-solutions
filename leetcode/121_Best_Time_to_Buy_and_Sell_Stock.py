class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        n = len(prices)
        buy, sell = 0, 1

        while buy < n and sell < n:
            if prices[buy] > prices[sell]:
                buy, sell = sell, sell + 1
                continue

            curr_profit = prices[sell] - prices[buy]
            if curr_profit > max_profit:
                max_profit = curr_profit
            sell += 1

        return max_profit
