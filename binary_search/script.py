def binary_search_recursive(input_list, pattern):
    if not input_list:
        return 'value not found'

    middle_idx = len(input_list) // 2
    middle_value = input_list[middle_idx]

    if middle_value == pattern:
        return middle_idx
    if middle_value > pattern:
        return binary_search_recursive(input_list[:middle_idx], pattern)
    else:
        result = binary_search_recursive(input_list[middle_idx + 1:], pattern)
        if result is str:
            return result
        return result + middle_idx + 1


def binary_search_pointers(input_list, pattern, left_pointer=None, right_pointer=None):
    left_pointer = 0 if left_pointer is None else left_pointer
    right_pointer = len(input_list) if right_pointer is None else right_pointer

    if left_pointer >= right_pointer:
        return 'value not found'

    middle_idx = (left_pointer + right_pointer) // 2
    middle_value = input_list[middle_idx]

    if middle_value == pattern:
        return middle_idx
    if middle_value > pattern:
        return binary_search_pointers(input_list, pattern, left_pointer, middle_idx)
    else:
        return binary_search_pointers(input_list, pattern, middle_idx + 1, right_pointer)
