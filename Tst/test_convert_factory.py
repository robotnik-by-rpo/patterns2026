import pytest
from datetime import datetime

from Src.Logics.convert_factory import convert_factory
from Src.Models.technical_map_model import technical_map_model
from Src.Logics.storage_manager import storage_manager
from Src.Core.exception import not_exist_exception
from Src.Dtos.report_type_dto import report_type_enum


def test_convert_factory_converts_simple_types():
    """Check factory returns"""
    # Preparation
    factory = convert_factory()

    # Action
    as_str = factory.convert("text")
    as_int = factory.convert(10)
    as_float = factory.convert(1.5)
    as_bool = factory.convert(True)

    # Verification
    assert as_str == "text"
    assert as_int == 10
    assert as_float == 1.5
    assert as_bool is True


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


def test_convert_factory_returns_none_for_none():
    """Check None value"""
    # Preparation
    factory = convert_factory()

    # Action
    result = factory.convert(None)

    # Verification
    assert result is None


def test_convert_factory_converts_enum_to_value():
    """Check Enum value"""
    # Preparation
    factory = convert_factory()

    # Action
    result = factory.convert(report_type_enum.TXT)

    # Verification
    assert result == "TXT"


def test_convert_factory_converts_list_of_models():
    """Check list of models -> list of dicts"""
    # Preparation
    factory = convert_factory()
    tech = technical_map_model.create_technical_map()

    # Action
    result = factory.convert([tech, tech])

    # Verification
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["id"] == tech.id
    assert result[1]["id"] == tech.id


def test_convert_factory_converts_reference_type():
    """Check factory delegates models to reference convertor"""
    # Preparation
    factory = convert_factory()
    tech = technical_map_model.create_technical_map()

    # Action
    result = factory.convert(tech)

    # Verification
    assert result["id"] == tech.id
    assert result["name"] == tech.name
    assert isinstance(result["recipe"], dict)
    assert isinstance(result["recipe"]["instruction"], list)
    assert isinstance(result["recipe"]["instruction"][0], str)


def test_convert_factory_converts_storage_manager():
    """Check factory handles objects with __dict__"""
    # Preparation
    factory = convert_factory()
    storage = storage_manager()

    # Action
    result = factory.convert(storage)

    # Verification
    assert "units_of_measurement" in result
    assert "warehouses" in result
    assert isinstance(result["warehouses"]["A"], list)


def test_convert_factory_rejects_unknown_type():
    """Check unsupported type raises"""
    # Preparation
    factory = convert_factory()

    # Action
    with pytest.raises(not_exist_exception) as exception:
        _ = factory.convert(b"bytes")

    # Verification
    assert "type of object" in str(exception.value)