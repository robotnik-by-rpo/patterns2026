from Src.Models.prepack_model import prepack_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Core.exception import arguments_exception
import pytest

def test_create_prepack():
    """Check creating perpack"""
    prepacks = prepack_model.create_prepack()
    names = ["nuggets","dumpligs"]
    bruttos = [200, 200]
    wastes = [20,20]
    g = unit_of_measurement_model.create_g()
    brands = ["The Golden Cockerel","We sculpt and cook"]
    categories = ["А","Б"]
    for i in range(0,2):
        assert prepacks[i].name == names[i]
        assert prepacks[i].brutto == bruttos[i]
        assert prepacks[i].waste == wastes[i]
        assert prepacks[i].brand == brands[i]
        assert prepacks[i].unit.name == g.name
        assert prepacks[i].category == categories[i] 


def test_cacl_netto_prepark_model():
    """Check netto after initing prepacks"""
    prepacks = prepack_model.create_prepack()
    assert prepacks[0].netto == 160.0

def test_setter_brutto_prepacks_model():
    """Check setter brutto of prepacks"""
    prepacks = prepack_model.create_prepack()
    new_brutto = 250.0
    prepacks[0].brutto = new_brutto
    assert prepacks[0].brutto == new_brutto
    assert prepacks[0].netto == 200.0

def test_setter_brand_prepacks_model():
    """Check setter brand of prepacks"""
    prepacks = prepack_model.create_prepack()
    new_brand = "Makfa 1"
    prepacks[0].brand = new_brand
    assert prepacks[0].brand == new_brand

def test_setter_waste_prepacks_model():
    """Check setter waste of prepacks"""
    prepacks = prepack_model.create_prepack()
    new_waste = 25.0
    prepacks[0].waste = new_waste
    assert prepacks[0].waste == new_waste
    assert prepacks[0].netto == 150.0

def test_set_null_brutto_prepacks_model():
    """Check set brutto None value"""
    prepacks = prepack_model.create_prepack()
    with pytest.raises(arguments_exception) as exception:
        prepacks[0].brutto = None

    assert "Wrong argument" in str(exception.value)
    assert "new brutto" in str(exception.value)

def test_set_null_waste_prepacks_model():
    """Check set waste None value"""
    prepacks = prepack_model.create_prepack()
    with pytest.raises(arguments_exception) as exception:
        prepacks[0].waste = None

    assert "Wrong argument" in str(exception.value)
    assert "new waste" in str(exception.value)

def test_setter_unit_prepacks_model():
    """Check setter unit of ingredients model"""
    prepacks = prepack_model.create_prepack()
    ml = unit_of_measurement_model.create_ml()
    prepacks[0].unit = ml
    assert prepacks[0].unit.name == ml.name