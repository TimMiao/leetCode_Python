class Solution:
    def reverse(self, x):
        num_list = []
        sign_list = []
        x_str = str(x)
        for i in range(0, len(x_str)):
            if x_str[i].isdigit():
                num_list.append(x_str[i])
            else:
                sign_list.append(x_str[i])
        num_list.reverse()
        if sign_list != []:
            new_list = sign_list + num_list
        else:
            new_list = num_list
        new_str = ''.join(new_list)
        x = int(new_str)
        if -2 ** 31 <= x and x <= (2 ** 31) - 1:
            return x
        else:
            return 0