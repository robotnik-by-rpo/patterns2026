from Src.Models.nomenclature_model import nomenclature_model
from Src.Core.exception import arguments_exception
from Src.Models.group_nomenclature_model import group_nomenclature_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
import pytest

def test_nomenclature_model_name_initing():
    """Check name after initting"""
    # Preparation
    group = group_nomenclature_model("Заказ")
    u1 = unit_of_measurement_model("грамм",1)
    u2 = unit_of_measurement_model("кг",1000, u1)
    n = nomenclature_model("Блюдо 1","Блюдо 1 от шефа", group,u2,"dish")

    # Action

    # verification
    assert n.name == "Блюдо 1"

def test_nomenclature_model_full_name_initing():
    """Check full name after initting"""
    # Preparation
    group = group_nomenclature_model("Заказ")
    u1 = unit_of_measurement_model("грамм",1)
    u2 = unit_of_measurement_model("кг",1000, u1)
    n = nomenclature_model("Блюдо 1","Блюдо 1 от шефа", group,u2,"dish")

    # Action

    # verification
    assert n.full_name == "Блюдо 1 от шефа"

def test_nomenclature_model_group_initing():
    """Check group of nomenclature after initting"""
    # Preparation
    group = group_nomenclature_model("Заказ")
    u1 = unit_of_measurement_model("грамм",1)
    u2 = unit_of_measurement_model("кг",1000, u1)
    n = nomenclature_model("Блюдо 1","Блюдо 1 от шефа", group,u2,"dish")

    # Action

    # verification
    assert n.group_of_nomenclature == group
    
def test_nomenclature_model_base_unit_initing():
    """Check base unit of measurement after initting"""
    # Preparation
    group = group_nomenclature_model("Заказ")
    u1 = unit_of_measurement_model("грамм",1)
    u2 = unit_of_measurement_model("кг",1000, u1)
    n = nomenclature_model("Блюдо 1","Блюдо 1 от шефа", group,u2,"dish")

    # Action

    # verification
    assert n.base_unit == u2

def test_nomenclature_model_type_of_position_initing():
    """Check type of position after initting"""
    # Preparation
    group = group_nomenclature_model("Заказ")
    u1 = unit_of_measurement_model("грамм",1)
    u2 = unit_of_measurement_model("кг",1000, u1)
    n = nomenclature_model("Блюдо 1","Блюдо 1 от шефа", group,u2,"dish")

    # Action

    # verification
    assert n.type_of_pos == "dish"


def test_nomenclature_model_name_null():
    """Check name on None value"""
    # Preparation

    # Action
    with pytest.raises(arguments_exception) as exception:
        group = group_nomenclature_model("Заказ")
        u1 = unit_of_measurement_model("грамм",1)
        u2 = unit_of_measurement_model("кг",1000, u1)
        _ = nomenclature_model(None,"Блюдо 1 от шефа", group,u2,"dish")

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "name" in str(exception.value)

def test_nomenclature_model_full_name_null():
    """Check full name on None value"""
    # Preparation

    # Action
    with pytest.raises(arguments_exception) as exception:
        group = group_nomenclature_model("Заказ")
        u1 = unit_of_measurement_model("грамм",1)
        u2 = unit_of_measurement_model("кг",1000, u1)
        _ = nomenclature_model("Блюдо 1",None, group,u2,"dish")

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "full name" in str(exception.value)

def test_nomenclature_model_base_unit_null():
    """Check base unit on None value"""
    # Preparation

    # Action
    with pytest.raises(arguments_exception) as exception:
        group = group_nomenclature_model("Заказ")
        _ = nomenclature_model("Блюдо 1","Блюдо 1 от шефа", group,None,"dish")

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "base unit" in str(exception.value)

def test_nomenclature_model_group_null():
    """Check group of nomenclature on None value"""
    # Preparation

    # Action
    with pytest.raises(arguments_exception) as exception:
        u1 = unit_of_measurement_model("грамм",1)
        u2 = unit_of_measurement_model("кг",1000, u1)
        _ = nomenclature_model("Блюдо 1","Блюдо 1 от шефа", None,u2,"dish")

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "group" in str(exception.value)

def test_nomenclature_model_type_of_position_null():
    """Check type of position on None value"""
    # Preparation

    # Action
    with pytest.raises(arguments_exception) as exception:
        group = group_nomenclature_model("Заказ")
        u1 = unit_of_measurement_model("грамм",1)
        u2 = unit_of_measurement_model("кг",1000, u1)
        _ = nomenclature_model("Блюдо 1","Блюдо 1 от шефа", group,u2,None)

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "type" in str(exception.value)


def test_nomenclature_model_name_setter():
    """Check setter name on the same value after setting"""
    # Preparation
    group = group_nomenclature_model("Заказ")
    u1 = unit_of_measurement_model("грамм",1)
    u2 = unit_of_measurement_model("кг",1000, u1)
    n = nomenclature_model("Блюдо 1","Блюдо 1 от шефа", group,u2,"dish")

    # Action
    n.name = "Блюдо 2"

    # verification
    assert n.name == "Блюдо 2"

def test_nomenclature_model_full_name_setter():
    """Check setter full name on the same value after setting"""
    # Preparation
    group = group_nomenclature_model("Заказ")
    u1 = unit_of_measurement_model("грамм",1)
    u2 = unit_of_measurement_model("кг",1000, u1)
    n = nomenclature_model("Блюдо 1","Блюдо 1 от шефа", group,u2,"dish")

    # Action
    n.full_name = "Блюдо 1 от повара"

    # verification
    assert n.full_name == "Блюдо 1 от повара"

def test_nomenclature_model_base_unit_setter():
    """Check setter base unit on the same value after setting"""
    # Preparation
    group = group_nomenclature_model("Заказ")
    u1 = unit_of_measurement_model("грамм",1)
    u2 = unit_of_measurement_model("кг",1000, u1)
    u3 = unit_of_measurement_model("мл",1)
    n = nomenclature_model("Блюдо 1","Блюдо 1 от шефа", group,u2,"dish")

    # Action
    n.base_unit = u3

    # verification
    assert n.base_unit == u3

def test_nomenclature_model_group_setter():
    """Check setter group of nomeclature on the same value after setting"""
    # Preparation
    group1 = group_nomenclature_model("Заказ")
    u1 = unit_of_measurement_model("грамм",1)
    u2 = unit_of_measurement_model("кг",1000, u1)
    n = nomenclature_model("Блюдо 1","Блюдо 1 от шефа", group1,u2,"dish")
    group2 = group_nomenclature_model("dish")

    # Action
    n.group_of_nomenclature = group2

    # verification
    assert n.group_of_nomenclature == group2

def test_nomenclature_model_type_of_position_setter():
    """Check setter type of position on the same value after setting"""
    # Preparation
    group = group_nomenclature_model("Заказ")
    u1 = unit_of_measurement_model("грамм",1)
    u2 = unit_of_measurement_model("кг",1000, u1)
    n = nomenclature_model("Блюдо 1","Блюдо 1 от шефа", group,u2,"dish")

    # Action
    n.type_of_pos = "product"

    # verification
    assert n.type_of_pos == "product"

def test_nomenclature_model_name_with_line_limitation():
    """Check name if it has lenght longer than 50"""
    # Preparation

    # Action
    with pytest.raises(arguments_exception) as exception:
        group = group_nomenclature_model("Заказ")
        u1 = unit_of_measurement_model("грамм",1)
        u2 = unit_of_measurement_model("кг",1000, u1)
        _ = nomenclature_model("1"*51,"Блюдо 1 от шефа", group,u2,"dish")

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "name" in str(exception.value)

def test_nomenclature_model_full_name_with_line_limitation():
    """Check full name if it has lenght longer than 255"""
    # Preparation

    # Action
    with pytest.raises(arguments_exception) as exception:
        group = group_nomenclature_model("Заказ")
        u1 = unit_of_measurement_model("грамм",1)
        u2 = unit_of_measurement_model("кг",1000, u1)
        _ = nomenclature_model("Блюдо 1","1"*256, group,u2,"dish")

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "full name" in str(exception.value)



