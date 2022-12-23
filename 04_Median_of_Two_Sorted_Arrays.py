class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        final_list = nums1 + nums2
        final_list.sort()
        if len(final_list) % 2 == 1:
            middle = final_list[int((len(final_list) - 1) / 2)]
            return middle
        elif len(final_list) % 2 == 0:
            middle = final_list[int((len(final_list) - 1) / 2)]
            the_middle = final_list[int((len(final_list) + 1) / 2)]
            final_median = (middle + the_middle) / 2
            return final_median