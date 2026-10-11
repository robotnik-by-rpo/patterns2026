from Src.Models.ingredient_model import ingredient_model
from Src.Core.exception import arguments_exception
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
import pytest

def test_create_ingredient_model():
    """Check creating ingredients"""
    # preparation
    ingredients = ingredient_model.create_ingredients()
    names = ["flour","water","yeast","salt"]

    #action

    # verification
    for i in range(0,4):
        assert ingredients[i].name == names[i]

def test_cacl_netto_ingredient_model():
    """Check netto after initing ingredient"""
    # preparation
    ingredients = ingredient_model.create_ingredients()
    
    #action
    
    # verification
    assert ingredients[0].netto == 187.5

def test_setter_brutto_ingredient_model():
    """Check setter brutto of ingredient"""
    # preparation
    ingredients = ingredient_model.create_ingredients()
    new_brutto = 200.0

    #action
    ingredients[0].brutto = new_brutto
    
    # verification
    assert ingredients[0].brutto == new_brutto
    assert ingredients[0].netto == new_brutto

def test_setter_brand_ingredient_model():
    """Check setter brand of ingredient"""
    # preparation
    ingredients = ingredient_model.create_ingredients()
    new_brand = "Makfa 1"
    
    #action
    ingredients[0].brand = new_brand
    
    # verification
    assert ingredients[0].brand == new_brand

def test_setter_waste_ingredient_model():
    """Check setter waste of ingredient"""
    # preparation
    ingredients = ingredient_model.create_ingredients()
    new_waste = 1.0
    
    #action
    ingredients[0].waste = new_waste
    
    # verification
    assert ingredients[0].waste == new_waste
    assert ingredients[0].netto == 185.625

def test_set_null_brutto_ingredient_model():
    """Check set brutto None value"""
    # preparation
    ingredients = ingredient_model.create_ingredients()

    #action
    with pytest.raises(arguments_exception) as exception:
        ingredients[0].brutto = None

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "new brutto" in str(exception.value)

def test_set_null_waste_ingredient_model():
    """Check set waste None value"""
    # preparation
    ingredients = ingredient_model.create_ingredients()
    
    #action
    with pytest.raises(arguments_exception) as exception:
        ingredients[0].waste = None
    
    # verification
    assert "Wrong argument" in str(exception.value)
    assert "new waste" in str(exception.value)

def test_setter_unit_ingredient_model():
    """Check setter unit of ingredients model"""
    # preparation
    ingredients = ingredient_model.create_ingredients()
    ml = unit_of_measurement_model.create_ml()
    
    #action
    ingredients[0].unit = ml

    # verification
    assert ingredients[0].unit.name == ml.name