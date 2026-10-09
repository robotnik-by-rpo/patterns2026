import pytest
from Src.Models.recipe_line_model import recipe_line_model
from Src.Models.ingredient_model import ingredient_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Core.exception import arguments_exception

def _make_component(brutto: float = 100.0, waste: float = 0.0):
    """Creating ingredients for testing"""
    g = unit_of_measurement_model.create_g()
    return ingredient_model("test_ingredient", brutto, waste, "test_brand", g)

def test_create_recipe_line_model():
    """Check creating recipe line"""
    component = _make_component(100.0)
    line = recipe_line_model(component, 100.0, 1.0)

    assert line.component is component
    assert line.quantity == 100.0
    assert line.share == 1.0


def test_default_share_recipe_line_model():
    """Check default share value is 1.0"""
    component = _make_component()
    line = recipe_line_model(component, 50.0)

    assert line.share == 1.0


def test_brutto_recipe_line_model():
    """Check brutto calculation with 1.0"""
    component = _make_component(100.0, 0.0)
    line = recipe_line_model(component, 100.0, 1.0)
    brutto = line.brutto

    assert brutto == 100.0


def test_netto_recipe_line_model():
    """Check netto calculation with 1.0"""
    component = _make_component(100.0, 0.0)
    line = recipe_line_model(component, 100.0, 1.0)
    netto = line.netto

    assert netto == 100.0


def test_brutto_with_share_recipe_line_model():
    """Check brutto calculation with 0.5"""
    component = _make_component(100.0, 0.0)
    line = recipe_line_model(component, 100.0, 0.5)
    brutto = line.brutto

    assert brutto == 50.0


def test_netto_with_share_recipe_line_model():
    """Check netto calculation with 0.5"""
    component = _make_component(100.0, 0.0)
    line = recipe_line_model(component, 100.0, 0.5)
    netto = line.netto

    assert netto == 50.0


def test_netto_with_waste_recipe_line_model():
    """Check netto calculation considering waste of component"""
    component = _make_component(100.0, 20.0)
    line = recipe_line_model(component, 100.0, 1.0)
    netto = line.netto

    assert netto == 80.0


def test_netto_with_waste_and_share_recipe_line_model():
    """Check netto calculation considering waste and share"""
    component = _make_component(200.0, 25.0)
    line = recipe_line_model(component, 200.0, 0.5)
    netto = line.netto

    assert netto == 75.0
def test_setter_component_recipe_line_model():
    """Check component setter"""
    first = _make_component(100.0)
    second = _make_component(200.0)
    line = recipe_line_model(first, 100.0)
    line.component = second

    assert line.component is second
    assert line.brutto == 200.0


def test_setter_quantity_recipe_line_model():
    """Check quantity setter"""
    component = _make_component(100.0)
    line = recipe_line_model(component, 100.0)
    line.quantity = 250.0

    assert line.quantity == 250.0


def test_setter_share_recipe_line_model():
    """Check share setter"""
    component = _make_component(100.0)
    line = recipe_line_model(component, 100.0, 1.0)
    line.share = 0.25

    assert line.share == 0.25
    assert line.brutto == 25.0

def test_set_null_component_recipe_line_model():
    """Check setting component to None"""
    component = _make_component()
    line = recipe_line_model(component, 100.0)
    with pytest.raises(arguments_exception) as exception:
        line.component = None

    assert "Wrong argument" in str(exception.value)
    assert "component" in str(exception.value)


def test_set_null_quantity_recipe_line_model():
    """Check setting quantity to None"""
    component = _make_component()
    line = recipe_line_model(component, 100.0)
    with pytest.raises(arguments_exception) as exception:
        line.quantity = None

    assert "Wrong argument" in str(exception.value)
    assert "quantity" in str(exception.value)


def test_set_zero_quantity_recipe_line_model():
    """Check setting quantity to zero"""
    component = _make_component()
    line = recipe_line_model(component, 100.0)
    with pytest.raises(arguments_exception) as exception:
        line.quantity = 0

    assert "Wrong argument" in str(exception.value)
    assert "quantity" in str(exception.value)


def test_set_share_above_one_recipe_line_model():
    """Check setting share above 1.0"""
    component = _make_component()
    line = recipe_line_model(component, 100.0)
    with pytest.raises(arguments_exception) as exception:
        line.share = 1.5

    assert "Wrong argument" in str(exception.value)
    assert "share" in str(exception.value)


def test_set_share_zero_recipe_line_model():
    """Check setting share to zero"""
    component = _make_component()
    line = recipe_line_model(component, 100.0)
    with pytest.raises(arguments_exception) as exception:
        line.share = 0

    assert "Wrong argument" in str(exception.value)
    assert "share" in str(exception.value)


def test_set_share_negative_recipe_line_model():
    """Check setting share to negative value"""
    component = _make_component()
    line = recipe_line_model(component, 100.0)
    with pytest.raises(arguments_exception) as exception:
        line.share = -0.5

    assert "Wrong argument" in str(exception.value)
    assert "share" in str(exception.value)
