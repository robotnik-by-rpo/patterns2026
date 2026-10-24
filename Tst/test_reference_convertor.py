import pytest
from Src.Logics.reference_convertor import reference_convertor
from Src.Logics.storage_manager import storage_manager
from Src.Models.ingredient_model import ingredient_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Models.technical_map_model import technical_map_model
from Src.Core.exception import not_exist_exception


def test_reference_convertor_converts_ingredient():
    """Check ingredient -> dict with unit nested"""
    # Preparation
    convertor = reference_convertor()
    g = unit_of_measurement_model.create_g()
    ingredient = ingredient_model.create_ingredients()[0]

    # Action
    result = convertor.convert(ingredient)

    # Verification
    assert result["id"] == ingredient.id
    assert result["name"] == ingredient.name
    assert result["brutto"] == ingredient.brutto
    assert result["netto"] == ingredient.netto
    assert isinstance(result["unit"], dict)
    assert result["unit"]["name"] == g.name


def test_reference_convertor_converts_technical_map_with_source_key():
    """Check tech map -> dict with 'source' key (not 'sourse')"""
    # Preparation
    convertor = reference_convertor()
    tech = technical_map_model.create_technical_map()

    # Action
    result = convertor.convert(tech)

    # Verification
    assert result["id"] == tech.id
    assert "source" in result
    assert "sourse" not in result
    assert isinstance(result["recipe"], dict)
    assert isinstance(result["company"], dict)


def test_reference_convertor_converts_storage_manager():
    """Check storage_manager -> dict with warehouses as list"""
    # Preparation
    convertor = reference_convertor()
    storage = storage_manager()

    # Action
    result = convertor.convert(storage)

    # Verification
    assert "units_of_measurement" in result   
    assert "nomenclatures" in result
    assert "warehouses" in result
    assert "groups_nomenclature" in result   
    assert "tech_maps" in result
    assert isinstance(result["warehouses"]["A"], list)
    assert len(result["warehouses"]["A"]) > 0
    assert isinstance(result["units_of_measurement"]["weight"], dict)


def test_reference_convertor_rejects_unknown_type():
    """Check unsupported type raises"""
    # Preparation
    convertor = reference_convertor()

    # Action
    with pytest.raises(not_exist_exception) as exception:
        _ = convertor.convert(b"bytes")

    # Verification
    assert "type of object" in str(exception.value)