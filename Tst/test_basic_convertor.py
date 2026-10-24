import pytest
from Src.Logics.basic_convertor import basic_convertor
from Src.Core.exception import not_exist_exception


def test_basic_convertor_converts_str():
    """Check str -> dict with 'line'"""
    # Preparation
    convertor = basic_convertor()

    # Action
    result = convertor.convert("hello")

    # Verification
    assert result == {"line": "hello"}


def test_basic_convertor_converts_int_and_float():
    """Check int and float -> dict"""
    # Preparation
    convertor = basic_convertor()

    # Action
    as_int = convertor.convert(42)
    as_float = convertor.convert(3.14)

    # Verification
    assert as_int == {"value_integer": 42}
    assert as_float == {"value_float": 3.14}


def test_basic_convertor_rejects_unknown_type():
    """Check unsupported type raises"""
    # Preparation
    convertor = basic_convertor()

    # Action
    with pytest.raises(not_exist_exception) as exception:
        _ = convertor.convert([1, 2, 3])

    # Verification
    assert "type of object" in str(exception.value)