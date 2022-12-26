class Solution:
    def intersection(self, nums1, nums2):
        new_nums = []
    
        final_list = []
    
        for i in range(0, len(nums1)):
            if nums1[i] in nums2:
                new_nums.append(nums1[i])
        the_set = set(new_nums)
        for num in the_set:
            final_list.append(num)
        return final_list