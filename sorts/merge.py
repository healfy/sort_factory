import typing
import operator
from .base import BaseSort, DEFAULT, BaseSortFactory


class MergeSort(BaseSort):
    name = 'merge'

    def sort(self, array: typing.List) -> typing.List:
        return self.merge_sort(array)

    def merge_sort(self, array, compare=operator.lt):
        if len(array) < 2:
            return array[:]
        else:
            middle = int(len(array) / 2)
            left = self.merge_sort(array[:middle], compare)
            right = self.merge_sort(array[middle:], compare)
            return self.merge(left, right, compare)

    @staticmethod
    def merge(left, right, compare):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if compare(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result


class MergeSortsFactory(BaseSortFactory):

    sorters = {
        DEFAULT: MergeSort
    }

    @classmethod
    def get_sorter(cls, name: str) -> typing.Type[BaseSort]:
        return cls.sorters[name]
