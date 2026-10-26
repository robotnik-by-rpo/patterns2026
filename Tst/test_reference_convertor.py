import pytest
from Src.Logics.convert_factory import convert_factory
from Src.Logics.storage_manager import storage_manager
from Src.Models.ingredient_model import ingredient_model
from Src.Models.technical_map_model import technical_map_model
from Src.Core.exception import not_exist_exception


def test_reference_convertor_converts_ingredient():
    """Check ingredient -> dict with unit nested"""
    # Preparation
    factory = convert_factory()
    ingredient = ingredient_model.create_ingredients()[0]

    # Action
    result = factory.convert(ingredient)

    # Verification
    assert result["name"] == "flour"
    assert result["brand"] == "Makfa"
    assert isinstance(result["unit"], dict)
    assert result["unit"]["name"] == "gram"


def test_reference_convertor_converts_technical_map_with_source_key():
    """Check tech map"""
    # Preparation
    factory = convert_factory()
    tech = technical_map_model.create_technical_map()

    # Action
    result = factory.convert(tech)

    # Verification
    assert "source" in result
    assert result["source"] == tech.source
    assert result["name"] == tech.name
    assert isinstance(result["recipe"], dict)
    assert isinstance(result["recipe"]["lines"], list)


def test_reference_convertor_converts_storage_manager():
    """Check storage_manager, dict with warehouses as list"""
    # Preparation
    factory = convert_factory()
    storage = storage_manager()

    # Action
    result = factory.convert(storage)

    # Verification
    assert "warehouses" in result
    assert isinstance(result["warehouses"], dict)
    assert isinstance(result["warehouses"]["A"], list)
    assert isinstance(result["warehouses"]["A"][0], dict)
    assert result["warehouses"]["A"][0]["name"] == "A01"


def test_reference_convertor_rejects_unknown_type():
    """Check unsupported type raises"""
    # Preparation
    factory = convert_factory()

    # Action
    with pytest.raises(not_exist_exception) as exception:
        _ = factory.convert(b"bytes")

    # Verification
    assert "type of object" in str(exception.value)