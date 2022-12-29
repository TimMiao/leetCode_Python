class Solution:
    def addDigits(self, num):
        if num < 10:
            return num
        final_num = num % 10
        floor_num = num // 10
        while floor_num > 9:
            final_num += floor_num % 10
            floor_num //= 10
        final_num += floor_num
        return self.addDigits(final_num)