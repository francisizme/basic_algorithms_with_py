from script import MaxHeap
from random import shuffle


def test_max_heap():
    list_int = [1, 2, 3, 4, 5, 6, 7, 8]
    shuffle(list_int)
    max_heap = MaxHeap()
    for i in list_int:
        max_heap.add(i)

    assert max_heap.get_list()[1] == 8
