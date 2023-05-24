class Solution:
    def sortArrayByParity(self, nums):
        even_nums = []
        odd_nums = []
        for num in nums:
            if num % 2 == 0:
                even_nums.append(num)
            if num % 2 == 1:
                odd_nums.append(num)
        final_nums = even_nums + odd_nums
        return final_nums