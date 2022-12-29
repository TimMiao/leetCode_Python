class Solution:
    def isPerfectSquare(self, num):
        x = 1
        if num == 0: 
            return True
        while x*x < num:
            x += 1
        if x * x == num:
            return True
        else:
            return False