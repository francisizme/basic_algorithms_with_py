from random import randrange


def quick_sort(arr, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(arr) - 1
    if start >= end:
        return arr

    # grab pivot
    pivot_idx = randrange(start, end)
    pivot_el = arr[pivot_idx]

    # move pivot to most-right to optimize the interation
    arr[pivot_idx], arr[end] = arr[end], arr[pivot_idx]
    # track pointer
    less_than_pivot_idx = start

    for i in range(start, end):
        if arr[i] < pivot_el:
            # if the el at i is less than pivot, swap it w/ the most-right of less than pivot
            arr[i], arr[less_than_pivot_idx] = arr[less_than_pivot_idx], arr[i]
            less_than_pivot_idx += 1
    # move the pivot back to correct position
    arr[end], arr[less_than_pivot_idx] = arr[less_than_pivot_idx], arr[end]
    quick_sort(arr, start, less_than_pivot_idx - 1)
    quick_sort(arr, less_than_pivot_idx + 1, end)
