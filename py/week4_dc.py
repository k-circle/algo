def max_crossing_sum(arr, l, m, h):
    sm = 0
    left_sum = -float('inf')

    for i in range(m, l - 1, -1):
        sm = sm + arr[i]
        if (sm > left_sum):
            left_sum = sm
    sm = 0
    right_sum = -float('inf')
    for i in range(m + 1, h + 1):
        sm = sm + arr[i]
        if (sm > right_sum):
            right_sum = sm
    return left_sum + right_sum


def max_subarray_sum(arr, l, h):
    if (l == h):
        return arr[l]
    m = (l + h) // 2
    return max(max_subarray_sum(arr, l, m),
               max_subarray_sum(arr, m + 1, h),
               max_crossing_sum(arr, l, m, h))


if __name__ == '__main__':
    arr = [2, -3, 4, -1, 7]
    n = len(arr)
    max_sum = max_subarray_sum(arr, 0, n - 1)
    print("Maximum contiguous sum is ", max_sum)
