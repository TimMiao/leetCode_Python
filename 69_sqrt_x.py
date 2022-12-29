class Solution:
    def mySqrt(self, x) :
        half = 1
        while half * half < x:
            half += 1
        if half * half > x:
            final = half - (half - (half - 1)) / 2
            final //= 1
            the_final = int(final)
            return the_final
        elif half * half == x and type(half) == float:
            half //= 1
            the_sqrt = int(half)
            return the_sqrt
        elif half * half == x and type(half) == int:
            return half