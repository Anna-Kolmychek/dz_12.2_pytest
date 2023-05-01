import pytest

from utils import arrs


@pytest.fixture
def arr_1_3():
    return [1, 2, 3]


@pytest.fixture
def arr_1_4():
    return [1, 2, 3, 4]


def test_get(arr_1_3):
    assert arrs.get(arr_1_3, 1, "test") == 2
    assert arrs.get(arr_1_3, -1, "test") == "test"
    assert arrs.get([], 0, "test") == "test"


def test_slice(arr_1_3, arr_1_4):
    assert arrs.my_slice(arr_1_4, 1, 3) == [2, 3]
    assert arrs.my_slice(arr_1_3, 1) == [2, 3]
    assert arrs.my_slice([], 1, 3) == []
    assert arrs.my_slice(arr_1_4, -4) == [1, 2, 3, 4]
    assert arrs.my_slice(arr_1_4, -5) == [1, 2, 3, 4]
