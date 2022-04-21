def bubble_sort(arr):
    for i in range(len(arr)):
        for index in range(len(arr) - i - 1):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
    return arr
