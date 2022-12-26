class Solution:
    def twoSum(self, nums, target):
        the_dict = {}
        the_list = []
        for idx in range(0, len(nums)):
            the_dict[nums[idx]] = idx
        for i in range(0, len(nums)):
            the_difference = target - nums[i]
            if the_difference in nums and the_dict[the_difference] != i:
                the_list.append(i)
                the_list.append(the_dict[the_difference])
                break
        return the_list