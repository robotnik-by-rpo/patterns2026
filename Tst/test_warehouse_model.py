from Src.Core.exception import arguments_exception
from Src.Models.building_model import building_model
from Src.Models.organization_model import organization_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Models.warehouse_model import warehouse_model
import pytest

def test_warehouse_model_name_initing():
    """Check name value after initing"""
    own = organization_model("Ромашка",'1'*10,'1'*9,'1'*20,"ООО")
    u1 = unit_of_measurement_model("см",1)
    u2 = unit_of_measurement_model("м",10000,u1)
    desc = building_model("Склад",150,u2,"г.Москва, ул.Колотушкина")
    ware = warehouse_model("Склад 1", own, desc)

    assert ware.name == "Склад 1"

def test_warehouse_model_owner_initing():
    """Check owner value after initing"""
    own = organization_model("Ромашка",'1'*10,'1'*9,'1'*20,"ООО")
    u1 = unit_of_measurement_model("см",1)
    u2 = unit_of_measurement_model("м",10000,u1)
    desc = building_model("Склад",150,u2,"г.Москва, ул.Колотушкина")
    ware = warehouse_model("Склад 1", own, desc)

    assert ware.warehouse_owner == own

def test_warehouse_model_description_initing():
    """Check description value after initing"""
    own = organization_model("Ромашка",'1'*10,'1'*9,'1'*20,"ООО")
    u1 = unit_of_measurement_model("см",1)
    u2 = unit_of_measurement_model("м",10000,u1)
    desc = building_model("Склад",150,u2,"г.Москва, ул.Колотушкина")
    ware = warehouse_model("Склад 1", own, desc)

    assert ware.description_of_building == desc


def test_warehouse_model_owner_null():
    """Check owner on None value"""
    with pytest.raises(arguments_exception) as exception:
        u1 = unit_of_measurement_model("см",1)
        u2 = unit_of_measurement_model("м",10000,u1)
        desc = building_model("Склад",150,u2,"г.Москва, ул.Колотушкина")
        ware = warehouse_model("Склад 1", None, desc)
    
    assert "Wrong argument" in str(exception.value)
    assert "owner" in str(exception.value)

def test_warehouse_model_description_null():
    """Check description on None value"""
    with pytest.raises(arguments_exception) as exception:
        own = organization_model("Ромашка",'1'*10,'1'*9,'1'*20,"ООО")
        ware = warehouse_model("Склад 1", own, None)
    
    assert "Wrong argument" in str(exception.value)
    assert "description" in str(exception.value)

def test_warehouse_model_name_setter():
    """Check setter name value after setting"""
    own = organization_model("Ромашка",'1'*10,'1'*9,'1'*20,"ООО")
    u1 = unit_of_measurement_model("см",1)
    u2 = unit_of_measurement_model("м",10000,u1)
    desc = building_model("Склад",150,u2,"г.Москва, ул.Колотушкина")
    ware = warehouse_model("Склад 1", own, desc)
    ware.name = "Склад 2"
    assert ware.name == "Склад 2"

def test_warehouse_model_owner_setter():
    """Check setter owner value after setting"""
    own1 = organization_model("Ромашка",'1'*10,'1'*9,'1'*20,"ООО")
    u1 = unit_of_measurement_model("см",1)
    u2 = unit_of_measurement_model("м",10000,u1)
    desc = building_model("Склад",150,u2,"г.Москва, ул.Колотушкина")
    ware = warehouse_model("Склад 1", own1, desc)
    own2 = organization_model("Ромашка 1",'1'*10,'1'*9,'1'*20,"ООО")
    ware.warehouse_owner = own2

    assert ware.warehouse_owner == own2

def test_warehouse_model_description_setter():
    """Check setter owner value after setting"""
    own = organization_model("Ромашка",'1'*10,'1'*9,'1'*20,"ООО")
    u1 = unit_of_measurement_model("см",1)
    u2 = unit_of_measurement_model("м",10000,u1)
    desc = building_model("Склад",150,u2,"г.Москва, ул.Колотушкина")
    desc2 = building_model("Склад",180,u1,"г.Иркутск, ул.Колотушкина")
    ware = warehouse_model("Склад 1", own, desc2)
    ware.description_of_building = desc2

    assert ware.description_of_building == desc2
