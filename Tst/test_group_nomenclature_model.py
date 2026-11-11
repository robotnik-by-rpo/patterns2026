from Src.Models.group_nomenclature_model import group_nomenclature_model
from Src.Core.exception import arguments_exception
import pytest

def test_group_nomenclature_model_empty_name():
    """Check name on empty string"""
    # Preparation

    # Action
    with pytest.raises(arguments_exception) as exception:
        _ = group_nomenclature_model("")

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "name" in str(exception.value)

def test_group_nomenclature_model_null_name():
    """Check name on null value"""
    # Preparation

    # Action
    with pytest.raises(arguments_exception) as exception:
        _ = group_nomenclature_model(None)

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "name" in str(exception.value)


def test_group_nomenclature_model_getting_name():
    """Check getter name on the same value after initing"""
    # Preparation
    group = group_nomenclature_model("Продукты")

    # Action

    # verification
    assert group.name == "Продукты"

def test_group_nomenclature_model_setting_name():
    """Check getter name on the same value after setting"""
    # Preparation
    group = group_nomenclature_model("Продукты")

    # Action
    group.name = "Товар"

    # verification
    assert group.name == "Товар"
