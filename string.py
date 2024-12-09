def _KMP_search(text, pattern, start_index):
    if len(text) < len(pattern):
        return -1
    if start_index > len(text):
        return -1

    p = [0] * len(pattern)
    j = 0
    i = 1

    while i < len(pattern):
        if pattern[j] == pattern[i]:
            j += 1
            p[i] = j
            i += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j]
    
    j = 0
    i = start_index
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1

    return -1

def find_min_shift(S, T):
    if len(S) != len(T):
        return -1
    double_S = S + S
    if T in double_S:
        shift_index = double_S.find(T)
        return shift_index % len(S)
    else:
        return -1
# S = "abcdef"
# T = "fabcde"
# print(find_min_shift(S, T))
