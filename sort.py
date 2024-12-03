def bubble(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:] + right[j:]
    return result

def merge_sort(list):
    if len(list) <= 1:
        return list
    M = len(list) // 2
    left = merge_sort(list[:M])
    right = merge_sort(list[M:])
    return _merge(left, right)
    
def quik(list):
    if len(list) <= 1:
        return list
    pivot = list[len(list) // 2]
    left = [x for x in list if x < pivot]
    middle = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]
    return quik(left) + middle + quik(right)
