class Solution(object):
    def tribonacci(self, n):
        
        if n <= 2:
            base = [0,1,1]
            return base[n]

        a, b, c = 0, 1, 1
        for i in range (3, n+1):
            new = a + b + c
            a = b
            b = c
            c = new 
        
        return c
