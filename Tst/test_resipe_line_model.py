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
    # preparation
    component = _make_component(100.0)
    line = recipe_line_model(component, 100.0, 1.0)

    #action

    # verification
    assert line.component is component
    assert line.quantity == 100.0
    assert line.share == 1.0


def test_default_share_recipe_line_model():
    """Check default share value is 1.0"""
    # preparation
    component = _make_component()
    line = recipe_line_model(component, 50.0)

    #action

    # verification
    assert line.share == 1.0


def test_brutto_recipe_line_model():
    """Check brutto calculation with 1.0"""
    # preparation
    component = _make_component(100.0, 0.0)
    line = recipe_line_model(component, 100.0, 1.0)
    brutto = line.brutto

    #action

    # verification
    assert brutto == 100.0


def test_netto_recipe_line_model():
    """Check netto calculation with 1.0"""
    # preparation
    component = _make_component(100.0, 0.0)
    line = recipe_line_model(component, 100.0, 1.0)
    netto = line.netto

    #action

    # verification
    assert netto == 100.0


def test_brutto_with_share_recipe_line_model():
    """Check brutto calculation with 0.5"""
    # preparation
    component = _make_component(100.0, 0.0)
    line = recipe_line_model(component, 100.0, 0.5)
    brutto = line.brutto

    #action

    # verification
    assert brutto == 50.0


def test_netto_with_share_recipe_line_model():
    """Check netto calculation with 0.5"""
    # preparation
    component = _make_component(100.0, 0.0)
    line = recipe_line_model(component, 100.0, 0.5)
    netto = line.netto

    #action

    # verification
    assert netto == 50.0


def test_netto_with_waste_recipe_line_model():
    """Check netto calculation considering waste of component"""
    # preparation
    component = _make_component(100.0, 20.0)
    line = recipe_line_model(component, 100.0, 1.0)
    netto = line.netto

    #action

    # verification
    assert netto == 80.0


def test_netto_with_waste_and_share_recipe_line_model():
    """Check netto calculation considering waste and share"""
    # preparation
    component = _make_component(200.0, 25.0)
    line = recipe_line_model(component, 200.0, 0.5)
    netto = line.netto

    #action

    # verification

    assert netto == 75.0
def test_setter_component_recipe_line_model():
    """Check component setter"""
    # preparation
    first = _make_component(100.0)
    second = _make_component(200.0)
    line = recipe_line_model(first, 100.0)

    #action
    line.component = second

    # verification
    assert line.component is second
    assert line.brutto == 200.0


def test_setter_quantity_recipe_line_model():
    """Check quantity setter"""
    # preparation
    component = _make_component(100.0)
    line = recipe_line_model(component, 100.0)

    #action
    line.quantity = 250.0

    # verification
    assert line.quantity == 250.0


def test_setter_share_recipe_line_model():
    """Check share setter"""
    # preparation
    component = _make_component(100.0)
    line = recipe_line_model(component, 100.0, 1.0)

    #action
    line.share = 0.25

    # verification
    assert line.share == 0.25
    assert line.brutto == 25.0

def test_set_null_component_recipe_line_model():
    """Check setting component to None"""
    # preparation
    component = _make_component()
    line = recipe_line_model(component, 100.0)
    
    #action
    with pytest.raises(arguments_exception) as exception:
        line.component = None

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "component" in str(exception.value)


def test_set_null_quantity_recipe_line_model():
    """Check setting quantity to None"""
    # preparation
    component = _make_component()
    line = recipe_line_model(component, 100.0)
    
    #action
    with pytest.raises(arguments_exception) as exception:
        line.quantity = None

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "quantity" in str(exception.value)


def test_set_zero_quantity_recipe_line_model():
    """Check setting quantity to zero"""
    # preparation
    component = _make_component()
    line = recipe_line_model(component, 100.0)
    
    #action
    with pytest.raises(arguments_exception) as exception:
        line.quantity = 0

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "quantity" in str(exception.value)


def test_set_share_above_one_recipe_line_model():
    """Check setting share above 1.0"""
    # preparation
    component = _make_component()
    line = recipe_line_model(component, 100.0)
    
    #action
    with pytest.raises(arguments_exception) as exception:
        line.share = 1.5

    assert "Wrong argument" in str(exception.value)
    assert "share" in str(exception.value)


def test_set_share_zero_recipe_line_model():
    """Check setting share to zero"""
    # preparation
    component = _make_component()
    line = recipe_line_model(component, 100.0)
    
    #action
    with pytest.raises(arguments_exception) as exception:
        line.share = 0

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "share" in str(exception.value)


def test_set_share_negative_recipe_line_model():
    """Check setting share to negative value"""
    # preparation
    component = _make_component()
    line = recipe_line_model(component, 100.0)
    
    #action
    with pytest.raises(arguments_exception) as exception:
        line.share = -0.5

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "share" in str(exception.value)

def test_set_invalid_component_recipe_line_model():
    """Компонент без brutto/netto должен отсекаться сеттером."""
    """Check component without brutto/netto must cut off setter"""
    # preparation
    component = _make_component()
    line = recipe_line_model(component, 100.0)
    bad = unit_of_measurement_model.create_g()

    # action
    with pytest.raises(arguments_exception) as exception:
        line.component = bad

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "component" in str(exception.value)
