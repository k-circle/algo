def selection_sort(arr):
    for i in range(len(arr)):
        m_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[m_idx]:
                m_idx = j
        if arr[i] > arr[m_idx]:
            arr[i], arr[m_idx] = arr[m_idx], arr[i]
    print(arr)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1], arr[j] = arr[j], arr[j+1]
            j -= 1
    print(arr)


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)


unsorted_array = [1, 9, 2, 6, 19, 8, 4]
selection_sort(unsorted_array)
insertion_sort(unsorted_array)
bubble_sort(unsorted_array)
