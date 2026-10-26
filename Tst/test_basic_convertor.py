import pytest
from Src.Logics.basic_convertor import basic_convertor
from Src.Core.exception import not_exist_exception


def test_basic_convertor_converts_str():
    """Check str"""
    # Preparation
    convertor = basic_convertor()

    # Action
    result = convertor.convert("hello")

    # Verification
    assert result == "hello"
    assert isinstance(result, str)


def test_basic_convertor_converts_int_and_float():
    """Check int and float"""
    # Preparation
    convertor = basic_convertor()

    # Action
    as_int = convertor.convert(42)
    as_float = convertor.convert(3.14)

    # Verification
    assert as_int == 42
    assert isinstance(as_int, int)
    assert as_float == 3.14
    assert isinstance(as_float, float)


def test_basic_convertor_converts_bool():
    """Check bool"""
    # Preparation
    convertor = basic_convertor()

    # Action
    as_true = convertor.convert(True)
    as_false = convertor.convert(False)

    # Verification
    assert as_true is True
    assert as_false is False


def test_basic_convertor_rejects_unknown_type():
    """Check unsupported type"""
    # Preparation
    convertor = basic_convertor()

    # Action
    with pytest.raises(not_exist_exception) as exception:
        _ = convertor.convert([1, 2, 3])

    # Verification
    assert "type of object" in str(exception.value)