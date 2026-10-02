from Src.Core.building import building
from Src.Core.exception import arguments_exception
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
import pytest

def test_building_name_initing():
    """Check name on the same value after initing"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    b1 = building("Ресторан",150,u_o_m2,"г. Москва ул. Колотушкина")

    assert b1.name == "Ресторан"

def test_building_square_initing():
    """Check square on the same value after initing"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    b1 = building("Ресторан",150,u_o_m2,"г. Москва ул. Колотушкина")

    assert b1.square == 150
    
def test_building_base_unit_initing():
    """Check base unit of measurement on the same value after initing"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    b1 = building("Ресторан",150,u_o_m2,"г. Москва ул. Колотушкина")

    assert b1.base_unit == u_o_m2

def test_building_address_initing():
    """Check address on the same value after initing"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    b1 = building("Ресторан",150,u_o_m2,"г. Москва ул. Колотушкина")

    assert b1.address == "г. Москва ул. Колотушкина"

def test_building_zero_square():
    """Check square on zero value"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    
    with pytest.raises(arguments_exception) as exception:
        _ = building("Ресторан",0,u_o_m2,"г. Москва ул. Колотушкина")

    assert "Wrong argument" in str(exception.value)
    assert "square" in str(exception.value)

def test_building_negative_square():
    """Check square on negative value"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    
    with pytest.raises(arguments_exception) as exception:
        _ = building("Ресторан",-150,u_o_m2,"г. Москва ул. Колотушкина")

    assert "Wrong argument" in str(exception.value)
    assert "square" in str(exception.value)


def test_building_empty_address():
    """Check address on empty string"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    
    with pytest.raises(arguments_exception) as exception:
        _ = building("Ресторан",150,u_o_m2,"")

    assert "Wrong argument" in str(exception.value)
    assert "address" in str(exception.value)

def test_building_null_base_unit():
    with pytest.raises(arguments_exception) as exception:
        _ = building("Ресторан",150,None,"г. Москва ул. Колотушкина")

    assert "Wrong argument" in str(exception.value)
    assert "unit" in str(exception.value)

def test_building_setter_square():
    """Check setter of square on the same value after setting"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    b1 = building("Ресторан",150,u_o_m2,"г. Москва ул. Колотушкина")
    b1.square = 156

    assert b1.square == 156

def test_building_setter_base_unit():
    """Check setter of base unit on the same value after setting"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    b1 = building("Ресторан",150,u_o_m2,"г. Москва ул. Колотушкина")
    u_o_m3 = unit_of_measurement_model("км",1e-10,u_o_m)
    b1.base_unit = u_o_m3

    assert b1.base_unit == u_o_m3

def test_building_setter_address():
    """Check setter of address on the same value after setting"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    b1 = building("Ресторан",150,u_o_m2,"г. Москва ул. Колотушкина")
    b1.address = "г.Иркутск"

    assert b1.address == "г.Иркутск"

def test_building_null_address():
    """Check address on the null value"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    with pytest.raises(arguments_exception) as exception:
        _ = building("Ресторан",150,u_o_m2,None)
    
    assert "Wrong argument" in str(exception.value)
    assert "address" in str(exception.value)


def test_building_null_name():
    """Check name on the null value"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    with pytest.raises(arguments_exception) as exception:
        _ = building(None,150,u_o_m2,"г. Москва ул. Колотушкина")
    
    assert "Wrong argument" in str(exception.value)
    assert "name" in str(exception.value)


