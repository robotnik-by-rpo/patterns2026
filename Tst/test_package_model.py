from Src.Models.package_model import package_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model

def test_create_package_model():
    """Check factory method for package"""
    # Preparation
    pack = package_model.create_package_paper()

    # Action

    # verification
    assert pack.measure == 3.5
    assert pack.name == "paper"
    assert pack.unit.name == unit_of_measurement_model.create_l().name


def test_setter_measure_package_model():
    """Check setter for measure"""
    # Preparation
    pack = package_model.create_package_paper()

    # Action
    pack.measure = 30.5

    # verification
    assert pack.measure == 30.5

def test_setter_unit_model():
    """Check setter for unit"""
    # Preparation
    pack = package_model.create_package_paper()
    new_unit = unit_of_measurement_model.create_m3()

    # Action
    pack.unit = new_unit
    
    # verification
    assert pack.unit.name == new_unit.name

