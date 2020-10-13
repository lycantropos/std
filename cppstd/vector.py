from typing import (Generic,
                    Iterable,
                    List,
                    Union,
                    overload)

from reprit.base import (generate_repr,
                         seekers)

from .hints import Domain


class Vector(Generic[Domain]):
    __slots__ = '_values'

    def __init__(self, *values: Domain) -> None:
        self._values = list(values)  # type: List[Domain]

    __repr__ = generate_repr(__init__,
                             field_seeker=seekers.complex_)

    def __delitem__(self, item: Union[int, slice]) -> None:
        del self._values[item]

    def __eq__(self, other: 'Vector') -> bool:
        return (self._values == other._values
                if isinstance(other, Vector)
                else NotImplemented)

    @overload
    def __getitem__(self, item: int) -> Domain:
        """Returns element by given index."""

    @overload
    def __getitem__(self, item: slice) -> 'Vector[Domain]':
        """Returns subvector by given slice."""

    def __getitem__(self, item):
        return self._values[item]

    def __len__(self) -> int:
        return len(self._values)

    @overload
    def __setitem__(self, item: int, value: Domain) -> None:
        """Sets element by given index to given value."""

    @overload
    def __setitem__(self, item: slice, values: Iterable[Domain]) -> None:
        """Sets subvector by given slice to given values."""

    def __setitem__(self, item, value):
        self._values[item] = value

    def push_back(self, value: Domain) -> None:
        self._values.append(value)