import pytest
from script import quick_sort
from random import shuffle


def test_quick_sort():
    unsorted_arr = [5, 6, 7, 4, 3, 1, 2, 8, 0, 9]
    shuffle(unsorted_arr)
    quick_sort(unsorted_arr)
    assert unsorted_arr == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
