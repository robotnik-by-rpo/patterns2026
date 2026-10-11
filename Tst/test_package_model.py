from Src.Models.package_model import package_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model

def test_create_package_model():
    """Check factory method for package"""
    pack = package_model.create_package_paper()
    assert pack.measure == 3.5
    assert pack.name == "paper"
    assert pack.unit.name == unit_of_measurement_model.create_l().name


def test_setter_measure_package_model():
    """Check setter for measure"""
    pack = package_model.create_package_paper()
    pack.measure = 30.5

    assert pack.measure == 30.5

def test_setter_unit_model():
    """Check setter for unit"""
    pack = package_model.create_package_paper()
    new_unit = unit_of_measurement_model.create_m3()
    pack.unit = new_unit
    
    assert pack.unit.name == new_unit.name

