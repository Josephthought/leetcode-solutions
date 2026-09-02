# 169. Majority Element

**Pattern:** Boyer-Moore Voting Algorithm

## Idea
Find the element that appears more than n/2 times in the array (guaranteed
to exist). A hash map can count occurrences and find it in O(n) space, but
there's a clever O(1) space trick: treat it like a tug-of-war. Keep a
`candidate` and a `count`. If count hits 0, pick the current number as the
new candidate. If the current number matches the candidate, increase count;
if not, decrease count. Even though the candidate can flip back and forth
along the way, the true majority element always survives as the final
candidate, because it outnumbers everything else combined.

## Key formula
candidate = None
count = 0
for num in nums:
    if count == 0:
        candidate = num
    count += 1 if num == candidate else -1
return candidate

## Complexity
- Time: O(n) — single pass through the array
- Space: O(1) — only two variables (candidate, count), doesn't grow with n

## Gotcha
Check `count == 0` BEFORE comparing the current number to candidate, not
after — the candidate can only change when count has hit zero. Also, this
algorithm only works because the problem guarantees a true majority element
exists; without that guarantee, the final candidate could be wrong.