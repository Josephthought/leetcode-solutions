# 122. Best Time to Buy and Sell Stock II

**Pattern:** Greedy

## Idea
Unlike the original Buy/Sell Stock problem, here you can buy and sell
multiple times (but only hold one share at a time). Instead of tracking
a single running minimum, look at every consecutive day-to-day price
change. Any time tomorrow's price is higher than today's, that gain is
profit you can capture by "buying" today and "selling" tomorrow. Adding
up every positive day-to-day change gives the same result as optimally
timing multiple buy/sell trades across the whole array.

## Key formula
total_profit = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:
        total_profit += prices[i] - prices[i-1]
return total_profit

## Complexity
- Time: O(n) — single pass comparing each day to the day before it
- Space: O(1) — just one running total variable, doesn't grow with input

## Gotcha
Start the loop at index 1, not 0 — you're comparing each day to the
previous one, so index 0 has no valid "day before" to compare against.