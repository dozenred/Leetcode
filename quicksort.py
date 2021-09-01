def quicksort(arr, low, high):
    if low < high:
        i = partition(arr, low, high)
        quicksort(arr, low, i-1)
        quicksort(arr, i+1, high)


def partition(arr, low, high):
    x = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] <= x:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


# 非递归版本
def quicksort1(arr, low, high):
    if low >= high:
        return
    stack = []
    stack.append(low)
    stack.append(high)
    while stack:
        l = stack.pop(0)
        h = stack.pop(0)
        if l >= h:
            continue
        i = l-1
        x = arr[h]
        for j in range(l, h):
            if arr[j] <= x:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[h] = arr[h], arr[i+1]
        stack.extend([l, i, i+2, h])


