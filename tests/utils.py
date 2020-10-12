from collections import deque
from functools import partial
from itertools import count
from typing import (Any,
                    Callable,
                    Iterable,
                    TypeVar)

from _cppstd import Vector as BoundVector
from hypothesis.strategies import SearchStrategy

Domain = TypeVar('Domain')
Range = TypeVar('Range')
Strategy = SearchStrategy
BoundVector = BoundVector


def equivalence(left: bool, right: bool) -> bool:
    return left is right


def identity(value: Domain) -> Domain:
    return value


def pack(function: Callable[..., Range]
         ) -> Callable[[Iterable[Domain]], Range]:
    return partial(apply, function)


def apply(function: Callable[..., Range],
          args: Iterable[Domain]) -> Range:
    return function(*args)


def capacity(iterable: Iterable[Any]) -> int:
    counter = count()
    # order matters: if `counter` goes first,
    # then it will be incremented even for empty `iterable`
    deque(zip(iterable, counter),
          maxlen=0)
    return next(counter)