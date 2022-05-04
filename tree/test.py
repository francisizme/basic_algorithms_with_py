from script import TreeNode
from bfs import bfs
from dfs import dfs
import sys
import io
import pytest


@pytest.fixture()
def test_tree_fxt():
    root = TreeNode('ancestor')
    dad = TreeNode('dad')
    mom = TreeNode('mom')
    me = TreeNode('me')
    sis1 = TreeNode('sis1')
    bro1 = TreeNode('bro1')
    sis2 = TreeNode('sis2')
    bro2 = TreeNode('bro2')

    mom.add_child(sis1)
    dad.add_child(sis2)
    mom.add_child(bro1)
    mom.add_child(bro2)
    mom.add_child(me)
    root.add_child(mom)
    root.add_child(dad)
    return root


@pytest.fixture()
def test_bfs_fxt():
    animal = TreeNode('animal')
    dog = TreeNode('dog')
    cat = TreeNode('cat')
    chihuahua = TreeNode('chihuahua')
    poodle = TreeNode('poodle')
    persian = TreeNode('persian')
    sphinx = TreeNode('sphinx')

    cat.add_child(persian)
    cat.add_child(sphinx)
    dog.add_child(chihuahua)
    dog.add_child(poodle)
    animal.add_child(dog)
    animal.add_child(cat)

    return animal


def test_tree(test_tree_fxt):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    test_tree_fxt.traverse()
    assert captured_output.getvalue().strip() == '\n'.join(
        ['ancestor', 'dad', 'sis2', 'mom', 'me', 'bro2', 'bro1', 'sis1'])
    sys.stdout = sys.__stdout__


def test_bfs(test_bfs_fxt):
    assert bfs(test_bfs_fxt, 'animal') == 'animal'
    assert bfs(test_bfs_fxt, 'dog') == 'animal/dog'
    assert bfs(test_bfs_fxt, 'persian') == 'animal/cat/persian'


def test_dfs(test_bfs_fxt):
    assert dfs(test_bfs_fxt, 'animal') == 'animal'
    assert dfs(test_bfs_fxt, 'dog') == 'animal/dog'
    assert dfs(test_bfs_fxt, 'persian') == 'animal/cat/persian'
