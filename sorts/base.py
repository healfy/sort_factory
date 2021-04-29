import abc
from typing import List, Dict, Type


DEFAULT = 'default'


class BaseSort(abc.ABC):
    name: str

    @abc.abstractmethod
    def sort(self, array: List) -> List:
        pass


class BaseSortFactory(abc.ABC):
    sorters: Dict[str, Type[BaseSort]]

    @classmethod
    @abc.abstractmethod
    def get_sorter(cls, name: str) -> Type[BaseSort]:
        pass

