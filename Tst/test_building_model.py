from Src.Models.building_model import building_model
from Src.Core.exception import arguments_exception
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
import pytest

def test_building_model_name_initing():
    """Check name on the same value after initing"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    building = building_model("Ресторан",150,u_o_m2,"г. Москва ул. Колотушкина")

    assert building.name == "Ресторан"

def test_building_model_square_initing():
    """Check square on the same value after initing"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    building = building_model("Ресторан",150,u_o_m2,"г. Москва ул. Колотушкина")

    assert building.square == 150
    
def test_building_model_base_unit_initing():
    """Check base unit of measurement on the same value after initing"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    building = building_model("Ресторан",150,u_o_m2,"г. Москва ул. Колотушкина")

    assert building.base_unit == u_o_m2

def test_building_model_address_initing():
    """Check address on the same value after initing"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    building = building_model("Ресторан",150,u_o_m2,"г. Москва ул. Колотушкина")

    assert building.address == "г. Москва ул. Колотушкина"

def test_building_model_zero_square():
    """Check square on zero value"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    
    with pytest.raises(arguments_exception) as exception:
        _ = building_model("Ресторан",0,u_o_m2,"г. Москва ул. Колотушкина")

    assert "Wrong argument" in str(exception.value)
    assert "square" in str(exception.value)

def test_building_model_negative_square():
    """Check square on negative value"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    
    with pytest.raises(arguments_exception) as exception:
        _ = building_model("Ресторан",-150,u_o_m2,"г. Москва ул. Колотушкина")

    assert "Wrong argument" in str(exception.value)
    assert "square" in str(exception.value)


def test_building_model_empty_address():
    """Check address on empty string"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    
    with pytest.raises(arguments_exception) as exception:
        _ = building_model("Ресторан",150,u_o_m2,"")

    assert "Wrong argument" in str(exception.value)
    assert "address" in str(exception.value)

def test_building_model_null_base_unit():
    with pytest.raises(arguments_exception) as exception:
        _ = building_model("Ресторан",150,None,"г. Москва ул. Колотушкина")

    assert "Wrong argument" in str(exception.value)
    assert "unit" in str(exception.value)

def test_building_model_setter_square():
    """Check setter of square on the same value after setting"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    building = building_model("Ресторан",150,u_o_m2,"г. Москва ул. Колотушкина")
    building.square = 156

    assert building.square == 156

def test_building_model_setter_base_unit():
    """Check setter of base unit on the same value after setting"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    building = building_model("Ресторан",150,u_o_m2,"г. Москва ул. Колотушкина")
    u_o_m3 = unit_of_measurement_model("км",1e-10,u_o_m)
    building.base_unit = u_o_m3

    assert building.base_unit == u_o_m3

def test_building_model_setter_address():
    """Check setter of address on the same value after setting"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    building = building_model("Ресторан",150,u_o_m2,"г. Москва ул. Колотушкина")
    building.address = "г.Иркутск"

    assert building.address == "г.Иркутск"

def test_building_model_null_address():
    """Check address on the null value"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    with pytest.raises(arguments_exception) as exception:
        _ = building_model("Ресторан",150,u_o_m2,None)
    
    assert "Wrong argument" in str(exception.value)
    assert "address" in str(exception.value)


def test_building_model_null_name():
    """Check name on the null value"""
    u_o_m = unit_of_measurement_model("см",1)
    u_o_m2 = unit_of_measurement_model("м",10000,u_o_m)
    with pytest.raises(arguments_exception) as exception:
        _ = building_model(None,150,u_o_m2,"г. Москва ул. Колотушкина")
    
    assert "Wrong argument" in str(exception.value)
    assert "name" in str(exception.value)


