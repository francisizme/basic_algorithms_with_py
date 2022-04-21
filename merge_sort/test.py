from script import merge_sort


def test_merge_sort():
    assert merge_sort([4, 3, 5, 6, 7, 1, 8, 9, 2]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
