from script import HashMap


def test_hash_map():
    hash_map = HashMap(4)
    hash_map.assign('abc', 'normal abc')
    hash_map.assign('cba', 'reverse abc')
    assert hash_map.retrieve('abc') == 'normal abc'
    assert hash_map.retrieve('cba') == 'reverse abc'
