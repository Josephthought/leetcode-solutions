# 121. Best Time to Buy and Sell Stock

**Pattern:** Two Pointers / Running Minimum

## Idea
Find the max profit from buying on one day and selling on a later day.
Track the lowest price seen so far as you go — at each day, check what
profit you'd make selling today versus that lowest price.

## Key formula
min_price = min(min_price, price[i])
max_profit = max(max_profit, price[i] - min_price)

## Complexity
- Time: O(n) — single pass
- Space: O(1) — just two tracking variables

## Gotcha
You must buy BEFORE you sell — tracking min_price as you move forward
naturally enforces that order, since you can't use a future low price
for a past sell.