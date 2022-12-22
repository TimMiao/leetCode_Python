def two_sum(numbers, target):
    for i in range(0, len(numbers)):
        idx_j_num = target - numbers[i]
        idx_i = i
        if idx_j_num in numbers:
            break
    idx_j = numbers.index(idx_j_num, idx_i + 1)
    return [idx_i + 1, idx_j + 1]