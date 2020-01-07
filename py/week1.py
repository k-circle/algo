def simple(arry, target):
    # simple search
    arry = [i for i in range(20)]
    for i in arry:
        print("%d steps" % i)
        if i == target:
            print("Found %d" % i)
            break


def binary_search(arry, target):
    # binary search
    l = 0  # left pointer
    r = len(arry) - 1  # right pointer
    step = 0
    while l <= r:
        step += 1
        mid = l + (r - l) // 2
        print("%d steps" % step)
        if target == arry[mid]:
            print("Found %d" % arry[mid])
            break
        elif arry[mid] < target:
            l = mid + 1
        else:
            r = mid - 1


if __name__ == '__main__':
    arry = [i for i in range(20)]
    target = 17
    simple(arry, target)
    binary_search(arry, target)
