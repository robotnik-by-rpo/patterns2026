from Src.Models.unit_of_measurement_model import unit_of_measurement_model
import pytest
from Src.Core.exception import arguments_exception

def test_unit_of_measurement_model_name_not_null():
    """after created class name isn't empty, if argument isn't empty string"""    
    # Preparation
    u_o_m = unit_of_measurement_model("грамм",1)

    # Action

    assert u_o_m.name != ""

def test_unit_of_measurement_model_coef_not_null():
    """after created class coefficient doesn't equals -1"""
    # Preparation
    u_o_m = unit_of_measurement_model("грамм",5)

    # Action

    assert u_o_m.coef != 1

def test_unit_of_measurement_model_base_not_null():
    """after created class base doesn't equals None"""
    # Preparation
    u_o_m1 = unit_of_measurement_model("грамм",1)
    u_o_m2 = unit_of_measurement_model("кг",1000,u_o_m1)

    # Action

    assert u_o_m2.base is not None

def test_unit_of_measurement_model_base_equals_attributes():
    """attributes of __base are equal to the passed class instance unit_of_measurement"""
    # Preparation
    u_o_m1 = unit_of_measurement_model("грамм",1)
    u_o_m2 = unit_of_measurement_model("кг",1000,u_o_m1)

    # Action

    assert u_o_m2.base is u_o_m1


def test_unit_measurement_model_default_coefficient():
    """Check default coef after initing"""
    # Preparation
    u_o_m = unit_of_measurement_model("грамм") 

    # Action

    assert u_o_m.coef == 1

def test_unit_measurement_model_default_negative_coefficient():
    """Check raise on negative coefficient"""
    # Preparation

    # Action
    with pytest.raises(arguments_exception) as exception:
        _ = unit_of_measurement_model("грамм",-2) 

    assert "Wrong argument" in str(exception.value)
    assert "coefficient" in str(exception.value)


def test_unit_of_measurement_model_create_without_base():
    """Check base, __base must be None"""
    # Preparation
    u_o_m = unit_of_measurement_model("грамм",1)

    # Action

    assert u_o_m.base is None

def test_unit_of_measurement_model_coefficient_zero():
    """Check raise on zero coefficient"""
    # Preparation

    # Action
    with pytest.raises(arguments_exception) as exception:
        _ = unit_of_measurement_model("грамм", 0)

    assert "Wrong argument" in str(exception.value)
    assert "coefficient" in str(exception.value)

def test_unit_of_measurement_model_id_not_null():
    """check id after initing"""
    # Preparation
    u_o_m = unit_of_measurement_model("грамм",1)

    # Action

    assert u_o_m.id != ""

def test_unit_of_measurement_model_name_correct():
    """check name after initting"""
    # Preparation
    u_o_m = unit_of_measurement_model("грамм",1)

    # Action

    # verification
    assert u_o_m.name == "грамм"

def test_unit_of_measurement_model_coef_correct():
    """check coef after initting"""
    # Preparation
    u_o_m = unit_of_measurement_model("грамм",102)

    # Action

    # verification
    assert u_o_m.coef == 102
    
def test_unit_common_coef_chain():
    """check coef mul by chain"""
    # Preparation
    g = unit_of_measurement_model("грамм", 1)
    kg = unit_of_measurement_model("кг", 1000, g)
    t = unit_of_measurement_model("т", 1000, kg)

    # Action


    # verification
    assert kg.common_coef == 1000
    assert t.common_coef == 1_000_000
