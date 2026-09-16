# 118. Pascal's Triangle

**Pattern:** Iterative Row Building

## Idea
Generate the first numRows rows of Pascal's Triangle, where each row starts
and ends with 1, and every middle number is the sum of the two numbers
above it. Build row by row: take the previous row, sum every pair of
neighboring numbers to get the middle values, and sandwich them between
two 1s to form the new row.

## Key formula
result = [[1]]
while len(result) < numRows:
    prev_row = result[-1]
    new_row = [1]
    for j in range(len(prev_row) - 1):
        new_row.append(prev_row[j] + prev_row[j + 1])
    new_row.append(1)
    result.append(new_row)
return result

## Complexity
- Time: O(n²) — the outer loop runs ~n times, and the inner loop grows
  longer each time (1, 2, 3, ..., n), summing to roughly n²/2 total work
- Space: O(n²) — the triangle stores every row, and total numbers across
  all rows also sums to roughly n²/2

## Gotcha
new_row.append(1) and result.append(new_row) must sit OUTSIDE the inner
for loop (matching its indentation, not nested inside it) — otherwise
the closing 1 gets appended multiple times, or a row gets added to
result before it's fully built.