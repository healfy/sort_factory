from typing import Dict, Type
from .base import DEFAULT, BaseSortFactory
from .merge import MergeSortsFactory
from .insert import InsertSortsFactory
from .select import SelectSortSortsFactory


class AbstractSortFactory:
    sorts_factories: Dict[str, Type[BaseSortFactory]] = {
        'merge': MergeSortsFactory,
        'select': SelectSortSortsFactory,
        'insert': InsertSortsFactory,
    }

    @classmethod
    def get_sorter(cls, engine_name: str):
        factory: Type[BaseSortFactory] = cls.sorts_factories[engine_name]
        return factory.get_sorter(DEFAULT)
