def sum_to_one_call_stack(n):
    result = 1
    call_stack = []
    while n != 1:
        call_stack.append({
            'n': n
        })
        n -= 1
    while len(call_stack) > 0:
        stack_item = call_stack.pop()
        result += stack_item['n']
    return result


print("Call Stack: " + str(sum_to_one_call_stack(4)))  # Should be 10
print("Call Stack: " + str(sum_to_one_call_stack(5)))  # Should be 15


def sum_to_one(n):
    if n <= 1:
        return n
    return n + sum_to_one(n - 1)


print(f"Recursion: {sum_to_one(4)}")  # should be 10
print(f"Recursion: {sum_to_one(5)}")  # should be 15


def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n - 1)


print(f"Factorial: {factorial(4)}")  # should be 24
print(f"Factorial: {factorial(5)}")  # should be 120


def power_set(lst):
    if len(lst) == 0:
        return [[]]
    ps_without_first = power_set(lst[1:])
    with_first = [[lst[0]] + el for el in ps_without_first]
    return with_first + ps_without_first


subset = ['1', '2', '3', '4']
print(f"Power Set: {power_set(subset)}")


def flatten(my_list):
    result = []
    for item in my_list:
        if isinstance(item, list):
            result += flatten(item)
        else:
            result.append(item)
    return result


list1 = [1, 3, [4], 5]
list2 = [1, [2], [[3]], [[4], 5]]
print(f"Original: {list1}, flatten: {flatten(list1)}")
print(f"Original: {list2}, flatten: {flatten(list2)}")


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f"Fibonacci 3 should be: {fibonacci(3)}")
print(f"Fibonacci 4 should be: {fibonacci(5)}")
print(f"Fibonacci 5 should be: {fibonacci(21)}")


def build_bst(my_list):
    if len(my_list) == 0:
        return "No Child"
    middle_idx = len(my_list) // 2
    middle_value = my_list[middle_idx]
    print("Middle index: " + str(middle_idx))
    print("Middle value: " + str(middle_value))
    tree_node = {
        'data': middle_value,
        'left_child': build_bst(my_list[:middle_idx]),
        'right_child': build_bst(my_list[middle_idx + 1:]),
    }
    return tree_node


def move_to_end(lst, val):
    result = []
    if len(lst) == 0:
        return []
    if lst[0] == val:
        result = move_to_end(lst[1:], val)
        result.append(lst[0])
    else:
        result.append(lst[0])
        result += move_to_end(lst[1:], val)
    return result


gem_list = ["Diamond", "Ruby", "Jade", "Amber"]
print(f"In this list {gem_list}, Ruby should be placed at the end")
print(move_to_end(gem_list, 'Ruby'))


def wrap_string(my_str, n):
    if n == 0:
        return my_str
    return f"<{wrap_string(my_str, n - 1)}>"


print(f"Wrap div with 3 brackets: {wrap_string('div', 3)}")
