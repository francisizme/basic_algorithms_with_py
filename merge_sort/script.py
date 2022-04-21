def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result += left
    if right:
        result += right
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle_idx = len(arr) // 2
    left_arr = merge_sort(arr[:middle_idx])
    right_arr = merge_sort(arr[middle_idx:])

    return merge(left_arr, right_arr)
