import typing
from .base import BaseSort, BaseSortFactory, DEFAULT


class InsertSort(BaseSort):

    def sort(self, array: typing.List) -> typing.List:
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array


class InsertSortsFactory(BaseSortFactory):

    sorters = {
        DEFAULT: InsertSort
    }

    @classmethod
    def get_sorter(cls, name: str) -> typing.Type[BaseSort]:
        return cls.sorters[name]
