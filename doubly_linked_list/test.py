import pytest
from script import DoublyLinkedList


def test_create_list():
    dll = DoublyLinkedList()
    assert dll is not None


def test_add_to_head():
    dll = DoublyLinkedList()
    assert dll.stringify_list() == ''
    dll.add_to_head('Francis')
    dll.add_to_head('is')
    dll.add_to_head('name')
    dll.add_to_head('My')
    assert dll.stringify_list() == '\n'.join(['My', 'name', 'is', 'Francis'])


def test_add_to_tail():
    dll = DoublyLinkedList()
    assert dll.stringify_list() == ''
    dll.add_to_tail('My')
    dll.add_to_tail('name')
    dll.add_to_tail('is')
    dll.add_to_tail('Francis')
    assert dll.stringify_list() == '\n'.join(['My', 'name', 'is', 'Francis'])


@pytest.fixture()
def dll():
    dll = DoublyLinkedList()
    dll.add_to_head('Francis')
    dll.add_to_head('is')
    dll.add_to_head('name')
    dll.add_to_head('My')
    return dll


def test_remove_head(dll):
    assert dll.stringify_list() == '\n'.join(['My', 'name', 'is', 'Francis'])
    dll.remove_head()
    assert dll.stringify_list() == '\n'.join(['name', 'is', 'Francis'])


def test_remove_tail(dll):
    assert dll.stringify_list() == '\n'.join(['My', 'name', 'is', 'Francis'])
    dll.remove_tail()
    assert dll.stringify_list() == '\n'.join(['My', 'name', 'is'])


def test_remove_by_value(dll):
    assert dll.stringify_list() == '\n'.join(['My', 'name', 'is', 'Francis'])
    dll.remove_by_value('is')
    assert dll.stringify_list() == '\n'.join(['My', 'name', 'Francis'])
