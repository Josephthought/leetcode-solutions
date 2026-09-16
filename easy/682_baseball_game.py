class Solution(object):
    def calPoints(self, operations):
        stack = []

        for i in operations:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            elif i == "C":
                stack.pop()
            elif i == "D":
                stack.append(stack[-1] * 2)
            elif i == "+":
                stack.append(stack[-1] + stack[-2])

        return sum(stack)       