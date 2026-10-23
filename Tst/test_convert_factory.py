import pytest
from datetime import datetime
from Src.Logics.convert_factory import convert_factory
from Src.Models.technical_map_model import technical_map_model
from Src.Core.exception import not_exist_exception


def test_convert_factory_converts_simple_types():
    """Check factory delegates str/int/float to basic convertor"""
    # Preparation
    factory = convert_factory()

    # Action
    as_str = factory.convert("text")
    as_int = factory.convert(10)
    as_float = factory.convert(1.5)

    # Verification
    assert as_str == {"line": "text"}
    assert as_int == {"value_integer": 10}
    assert as_float == {"value_dot": 1.5}


def test_convert_factory_converts_datetime():
    """Check factory delegates datetime to datetime convertor"""
    # Preparation
    factory = convert_factory()
    value = datetime(2025, 9, 8, 10, 0, 0)

    # Action
    result = factory.convert(value)

    # Verification
    assert result["datetime"] == value.isoformat()
    assert result["year"] == 2025


def test_convert_factory_converts_reference_type():
    """Check factory delegates models to reference convertor"""
    # Preparation
    factory = convert_factory()
    tech = technical_map_model.create_technical_map()

    # Action
    result = factory.convert(tech)

    # Verification
    assert result["id"] == tech.id
    assert "recipe" in result
    assert "source" in result


def test_convert_factory_rejects_unknown_type():
    """Check unsupported type raises"""
    # Preparation
    factory = convert_factory()

    # Action
    with pytest.raises(not_exist_exception) as exception:
        _ = factory.convert([1, 2, 3])

    # Verification
    assert "type convert" in str(exception.value)