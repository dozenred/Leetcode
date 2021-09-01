def heaphelp(arr, index, start, end):
    if index >= end:
        return
    largest = index
    if 2*index + 1 < end and arr[2*index+1] > arr[largest]:
        largest = 2*index + 1
    if 2*index+2 < end and arr[2*index+2] > arr[largest]:
        largest = 2*index + 2
    arr[largest], arr[index] = arr[index], arr[largest]
    heaphelp(arr, largest, start, end)


def heapsort(arr, start, end):
    n = len(arr)
    mid = n//2 - 1
    for i in range(mid, -1, -1):
        heaphelp(arr, i, 0, n)
    arr[0], arr[-1] = arr[-1], arr[0]

    for i in range(n-2, -1, -1):
        heaphelp(arr, 0, 0, i+1)
        arr[0], arr[i] = arr[i], arr[0]
