class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
           return 0

        min_price = float('inf')  # Initialize with a very high value
        max_profit = 0

        for price in prices:
            if price < min_price:
               min_price = price  # Update min_price if current price is lower
            elif price - min_price > max_profit:
               max_profit = price - min_price  # Update max_profit if current profit is higher

        return max_profit


        
