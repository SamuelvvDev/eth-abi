from hypothesis import given
import hypothesis.strategies as st

from eth_abi import (
    encode_abi,
    decode_abi,
    encode_single,
    decode_single,
)

from .abi_type_strategies import (
    uint_strs,
    uint_values,
)


@given(uint_strs, uint_values)
def test_always_positive_multi(_type, value):
    """
    Tests round trip encoding and decoding for basic types and lists of basic
    types.
    """
    assert value >= 0

    encoded_value = encode_abi([_type], [value])
    decoded_value = decode_abi([_type], encoded_value)

    assert decoded_value[0] >= 0


@given(uint_strs, uint_values)
def test_always_positive_single(_type, value):
    """
    Tests round trip encoding and decoding for basic types and lists of basic
    types.
    """
    assert value >= 0

    encoded_value = encode_single(_type, value)
    decoded_value = decode_single(_type, encoded_value)

    assert decoded_value >= 0
