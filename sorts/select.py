import typing
from .base import BaseSort, DEFAULT, BaseSortFactory


class SelectSort(BaseSort):

    def sort(self, array: typing.List) -> typing.List:
        for i in range(len(array) - 1):
            m = i
            j = i + 1
            while j < len(array):
                if array[j] < array[m]:
                    m = j
                j = j + 1
            array[i], array[m] = array[m], array[i]
        return array


class SelectSortSortsFactory(BaseSortFactory):

    sorters = {
        DEFAULT: SelectSort
    }

    @classmethod
    def get_sorter(cls, name: str) -> typing.Type[BaseSort]:
        return cls.sorters[name]
