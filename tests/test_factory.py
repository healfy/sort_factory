import typing
import pytest

from sorts import AbstractSortFactory, BaseSort


@pytest.mark.parametrize('sort', ['merge', 'select', 'insert'])
def test_sorter_factory(sort):
    array = [1, 4, 7, 9, 0, 2, 3, 6, 10]
    sorter: typing.Type[BaseSort] = AbstractSortFactory.get_sorter(sort)
    assert sorter.name == sort

    result = sorter().sort([1, 4, 7, 9, 0, 2, 3, 6, 10])

    assert result == sorted(array)
