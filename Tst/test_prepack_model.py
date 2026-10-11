from Src.Models.prepack_model import prepack_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Core.exception import arguments_exception
import pytest

def test_create_prepack():
    """Check creating perpack"""
    # preparation
    prepacks = prepack_model.create_prepack()
    names = ["nuggets","dumpligs"]
    bruttos = [200, 200]
    wastes = [20,20]
    g = unit_of_measurement_model.create_g()
    brands = ["The Golden Cockerel","We sculpt and cook"]
    categories = ["А","Б"]

    #action

    # verification
    for i in range(0,2):
        assert prepacks[i].name == names[i]
        assert prepacks[i].brutto == bruttos[i]
        assert prepacks[i].waste == wastes[i]
        assert prepacks[i].brand == brands[i]
        assert prepacks[i].unit.name == g.name
        assert prepacks[i].category == categories[i] 


def test_cacl_netto_prepark_model():
    """Check netto after initing prepacks"""
    # preparation
    prepacks = prepack_model.create_prepack()

    #action

    # verification
    assert prepacks[0].netto == 160.0

def test_setter_brutto_prepacks_model():
    """Check setter brutto of prepacks"""
    # preparation
    prepacks = prepack_model.create_prepack()
    new_brutto = 250.0

    #action
    prepacks[0].brutto = new_brutto

    # verification
    assert prepacks[0].brutto == new_brutto
    assert prepacks[0].netto == 200.0

def test_setter_brand_prepacks_model():
    """Check setter brand of prepacks"""
    # preparation
    prepacks = prepack_model.create_prepack()
    new_brand = "Makfa 1"

    #action
    prepacks[0].brand = new_brand
    
    # verification
    assert prepacks[0].brand == new_brand

def test_setter_waste_prepacks_model():
    """Check setter waste of prepacks"""
    # preparation
    prepacks = prepack_model.create_prepack()
    new_waste = 25.0

    #action
    prepacks[0].waste = new_waste
    
    # verification
    assert prepacks[0].waste == new_waste
    assert prepacks[0].netto == 150.0

def test_set_null_brutto_prepacks_model():
    """Check set brutto None value"""
    # preparation
    prepacks = prepack_model.create_prepack()

    #action
    with pytest.raises(arguments_exception) as exception:
        prepacks[0].brutto = None

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "new brutto" in str(exception.value)

def test_set_null_waste_prepacks_model():
    """Check set waste None value"""
    # preparation
    prepacks = prepack_model.create_prepack()

    #action
    with pytest.raises(arguments_exception) as exception:
        prepacks[0].waste = None

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "new waste" in str(exception.value)

def test_setter_unit_prepacks_model():
    """Check setter unit of ingredients model"""
    # preparation
    prepacks = prepack_model.create_prepack()
    ml = unit_of_measurement_model.create_ml()

    #action
    prepacks[0].unit = ml

    # verification
    assert prepacks[0].unit.name == ml.name