from hypothesis import given

from tests.utils import (BoundPortedVectorsPair,
                         are_bound_ported_vector_iterators_equal)
from . import strategies


@given(strategies.vectors_pairs)
def test_basic(pair: BoundPortedVectorsPair) -> None:
    bound, ported = pair

    bound_result, ported_result = bound.crbegin(), ported.crbegin()

    assert are_bound_ported_vector_iterators_equal(bound_result, bound.crend(),
                                                   ported_result,
                                                   ported.crend())
