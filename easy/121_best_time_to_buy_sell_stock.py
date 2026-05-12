# LeetCod #121 - Best Tie to buy and sell stock
# Difficulty:  Easy
#Time: 0(n) Space: 0(1)
#Solved: May 2026
# Runtime: Beats 74.91%

class Solution:
    def maxProfit(self, prices):

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit,profit)

        return max_profit         
