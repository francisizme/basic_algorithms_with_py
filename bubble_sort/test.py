from script import bubble_sort


def test_bubble_sort():
    assert bubble_sort([4, 3, 5, 6, 7, 1, 8, 9, 2]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
