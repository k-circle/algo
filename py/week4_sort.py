def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    tmp = []

    while left and right:
        if left[0] <= right[0]:
            tmp.append(left.pop(0))
        else:
            tmp.append(right.pop(0))
    if left:
        tmp += left
    if right:
        tmp += right
    return tmp


if __name__ == '__main__':
    arr = [1, 4, 2, 11, 6, 10, -1, 0]
    cards = [(7, "S"), (5, "H"), (2, "H"), (5, "S")]
    print(quick_sort(arr))
    print(merge_sort(arr))

