from Src.Logics.storage_manager import storage_manager
from Src.Core.exception import operation_exception

def test_equals_storage_manager():
    """Check equals two storage managers after initing """
    instance1 = storage_manager()
    instance2 = storage_manager()

    assert instance1 == instance2

def test_equals_nomenclature_storage_manager():
    """Check equals nomenclatures after initing two storage managers"""    
    instance1 = storage_manager()
    instance2 = storage_manager()

    assert instance1.nomenclatures == instance2.nomenclatures

def test_equals_group_storage_manager():
    """Check equals groups after initing two storage managers"""    
    instance1 = storage_manager()
    instance2 = storage_manager()

    assert instance1.groups_nomenclature == instance2.groups_nomenclature

def test_equals_units_of_measurement_storage_manager():
    """Check equals nomenclatures after initing two storage managers"""    
    instance1 = storage_manager()
    instance2 = storage_manager()

    assert instance1.units_of_measurement == instance2.units_of_measurement


def test_equals_company__storage_manager():
    """Check equals companies after initing two storage managers"""    
    instance1 = storage_manager()
    instance2 = storage_manager()

    assert instance1.company == instance2.company

def test_equals_warehouses_storage_manager():
    """Check equals warehouses after initing two storage managers"""    
    instance1 = storage_manager()
    instance2 = storage_manager()

    assert instance1.warehouses == instance2.warehouses

def test_change_is_first_after_initing_storage_manager():
    """Check flag is_first after initing storage manager"""
    instance1 = storage_manager()
    assert instance1.is_first == False

def test_storage_units_of_measurement_unique():
    """Check unique units of measuremet"""
    instance = storage_manager()
    for _, units in instance.units_of_measurement.items():
        assert len(units) == len(set(id(u) for u in units.values()))

def test_storage_nomenclatures_unique():
    """Check unique nomenclature"""
    instance = storage_manager()
    for _, items in instance.nomenclatures.items():
        assert len(items) == len(set(id(n) for n in items))