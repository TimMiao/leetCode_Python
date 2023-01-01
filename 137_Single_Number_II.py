class Solution:
    def singleNumber(self, nums):
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        for key, value in num_dict.items():
            if value == min(num_dict.values()):
                return key