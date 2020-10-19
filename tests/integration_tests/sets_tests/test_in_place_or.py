from hypothesis import given

from tests.utils import (BoundPortedSetsPair,
                         are_bound_ported_sets_equal)
from . import strategies


@given(strategies.sets_pairs, strategies.sets_pairs)
def test_basic(first_pair: BoundPortedSetsPair,
               second_pair: BoundPortedSetsPair) -> None:
    first_bound, first_ported = first_pair
    second_bound, second_ported = second_pair

    first_bound |= second_bound
    first_ported |= second_ported

    assert are_bound_ported_sets_equal(first_bound, first_ported)
