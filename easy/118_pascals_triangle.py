class Solution(object):
    def generate(self, numRows):
        result = [[1]]

        while len(result) < numRows:
            prev_row = result[-1]
            new_row = [1]
            for j in range(len(prev_row) - 1):
                new_row.append(prev_row[j] + prev_row[j + 1])
            new_row.append(1)
            result.append(new_row)

        return result