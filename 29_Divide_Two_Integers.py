class Solution:
    def divide(self, dividend, divisor):
        if (dividend >= 0 and divisor > 0) or (dividend <= 0 and divisor < 0):
            if dividend == 0:
                return 0
            the_quotient, the_remainder = divmod(dividend, divisor)
            if the_quotient > (2 ** 31) - 1:
                the_quotient = (2 ** 31) - 1
                return the_quotient
            elif the_quotient < -2 ** 31:
                the_quotient = -2 ** 31
                return the_quotient
            else:
                return the_quotient
        elif dividend <= 0 and divisor > 0:
            if dividend == 0:
                return 0
            abs_dividend = abs(dividend)
            the_quotient, the_remainder = divmod(abs_dividend, divisor)
            final_quotient = - the_quotient
            if final_quotient > (2 ** 31) - 1:
                final_quotient = (2 ** 31) - 1
                return final_quotient
            elif final_quotient < -2 ** 31:
                final_quotient = -2 ** 31
                return final_quotient
            else:
                return final_quotient
        elif dividend >= 0 and divisor < 0:
            if dividend == 0:
                return 0
            abs_divisor = abs(divisor)
            the_quotient, the_remainder = divmod(dividend, abs_divisor)
            final_quotient = - the_quotient
            if final_quotient > (2 ** 31) - 1:
                final_quotient = (2 ** 31) - 1
                return final_quotient
            elif final_quotient < -2 ** 31:
                final_quotient = -2 ** 31
                return final_quotient
            else:
                return final_quotient