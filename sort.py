def bubble(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


def merge(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        merge(left)
        merge(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
            
def quik(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        left = [x for x in list[1:] if x < pivot]
        right = [x for x in list[1:] if x >= pivot]
        return quik(left) + [pivot] + quik(right)