class Solution:
    def findArray(self, pref):
        if len(pref) <= 1:
            return pref
        final_list =[]
        final_list.append(pref[0])
        new_int = pref[1] ^ pref[0]
        final_list.append(new_int)
        for i in range(2, len(pref)):
            new_int = pref[i] ^ pref[i - 1]
            final_list.append(new_int)
        return final_list