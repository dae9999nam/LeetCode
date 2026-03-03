class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0
        l = len(prices)
        for i in range(1, l):
            price = prices[i]
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
            if price < min_price:
                min_price = price
        return max_profit

            


