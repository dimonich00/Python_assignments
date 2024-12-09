from day5 import data_count


def test_counter():
    res = data_count({"test": "AAAACCCCTTTT"})
    assert res == [4, 4, 0, 4, 0, 12]


def test_counter2():
    res = data_count({"test": "GX"})
    assert res == [0, 0, 1, 0, 1, 2]
