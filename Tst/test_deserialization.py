from Src.Logics.convert_factory import convert_factory
import json
from Src.Logics.storage_manager import storage_manager

def test_warehouses_from_storage_manager_json():
    """Check deserialization warehouses from storage manager json"""
    # Preparation
    with open("Examples/json/storage_manager.json", encoding="utf-8") as f:
        raw = json.load(f)
    raw_wh = raw["warehouses"]
    ref_wh = storage_manager().warehouses

    # Action
    expected = sum(len(items) for items in raw_wh.values())

    # Verification
    assert set(raw_wh.keys()) == set(ref_wh.keys())
    for group, items in raw_wh.items():
        assert len(items) == len(ref_wh[group])
    checked = 0
    factory = convert_factory()
    for group, items in raw_wh.items():
        for index, data in enumerate(items):
            obj = factory.deserialize(data)
            ref = ref_wh[group][index]
            _assert_warehouse(obj, ref)
            checked += 1

    assert checked == expected


def test_tech_maps_from_storage_manager_json():
    """Check deserialization tech maps from storage manager json"""
    # Preparation
    with open("Examples/json/storage_manager.json", encoding="utf-8") as f:
        raw = json.load(f)
    raw_tm = raw["tech_maps"]
    ref_tm = storage_manager().tech_maps

    # Action
    expected = len(raw_tm)

    # Verification
    assert set(raw_tm.keys()) == set(ref_tm.keys())
    checked = 0
    factory = convert_factory()
    for name, data in raw_tm.items():
        obj = factory.deserialize(data)
        ref = ref_tm[name]
        _assert_tech_map(obj, ref)
        checked += 1

    assert checked == expected


def test_unit_from_storage_manager_json():
    """Check deserialization unit from storage manager json"""
    # Preparation
    with open("Examples/json/storage_manager.json", encoding="utf-8") as f:
        raw = json.load(f)
    kg_raw = raw["units_of_measurement"]["weight"]["kilogram"]
    obj = convert_factory().deserialize(kg_raw)
    ref = storage_manager().units_of_measurement["weight"]["kilogram"]

    # Action
    
    # Verification
    _assert_unit(obj, ref)   

def test_company_from_storage_manager_json():
    """Check deserialization company from storage manager json"""
    # Preparation
    with open("Examples/json/storage_manager.json", encoding="utf-8") as f:
        raw = json.load(f)
    org_raw = raw["company"]
    obj = convert_factory().deserialize(org_raw)
    ref = storage_manager().company

    # Action

    # Verification
    _assert_organization(obj, ref)

def test_nomenclature_from_storage_manager_json():
    """Check deserialization nomeclatures from storage manager json"""

    # Preparation
    with open("Examples/json/storage_manager.json", encoding="utf-8") as f:
        raw = json.load(f)
    raw_noms = raw["nomenclatures"]
    ref_noms = storage_manager().nomenclatures

    # Action
    expected = sum(len(items) for items in raw_noms.values())

    # Verification
    assert set(raw_noms.keys()) == set(ref_noms.keys())
    for group, items in raw_noms.items():
        assert set(items.keys()) == set(ref_noms[group].keys())
    checked = 0
    factory = convert_factory()
    for group, items in raw_noms.items():
        for name, data in items.items():
            obj = factory.deserialize(data)
            ref = ref_noms[group][name]
            _assert_nomenclature(obj, ref)
            checked += 1
    
    assert checked == expected
    

def _assert_unit(a, b):
    """Call asserts for unit"""
    assert type(a).__name__ == type(b).__name__
    assert a.name == b.name
    assert a.coef == b.coef
    assert a.common_coef == b.common_coef
    assert (a.base is None) == (b.base is None)
    if a.base is not None:
        _assert_unit(a.base, b.base)

def _assert_group(a, b):
    """Call asserts for group"""
    assert type(a).__name__ == type(b).__name__
    assert a.name == b.name

def _assert_nomenclature(a, b):
    """Call asserts for nomenclature"""
    assert type(a).__name__ == type(b).__name__
    assert a.name == b.name
    assert a.full_name == b.full_name
    assert a.type_of_pos == b.type_of_pos
    _assert_group(a.group_of_nomenclature, b.group_of_nomenclature)
    _assert_unit(a.base_unit, b.base_unit)

def _assert_organization(a, b):
    """Call asserts for organization"""
    assert type(a).__name__ == type(b).__name__
    assert a.name == b.name
    assert a.inn == b.inn
    assert a.bic == b.bic
    assert a.current_account == b.current_account
    assert a.form_of_ownership == b.form_of_ownership


def _assert_building(a, b):
    """Call asserts for building"""
    assert type(a).__name__ == type(b).__name__
    assert a.name == b.name
    assert a.address == b.address
    assert a.square == b.square
    _assert_unit(a.base_unit, b.base_unit)


def _assert_warehouse(a, b):
    """Call asserts for warehouse"""
    assert type(a).__name__ == type(b).__name__
    assert a.name == b.name
    _assert_organization(a.warehouse_owner, b.warehouse_owner)
    _assert_building(a.description_of_building, b.description_of_building)


def _assert_product(a, b):
    """Call asserts for product fields"""
    assert a.name == b.name
    assert a.brand == b.brand
    assert a.brutto == b.brutto
    assert a.netto == b.netto
    assert a.waste == b.waste
    _assert_unit(a.unit, b.unit)


def _assert_recipe_line(a, b):
    """Call asserts for recipe line"""
    assert type(a).__name__ == type(b).__name__
    assert a.quantity == b.quantity
    assert a.share == b.share
    _assert_product(a.component, b.component)
    assert type(a.component).__name__ == type(b.component).__name__


def _assert_recipe(a, b):
    """Call asserts for recipe"""
    assert type(a).__name__ == type(b).__name__
    assert a.name == b.name
    assert a.instruction == b.instruction
    assert len(a.lines) == len(b.lines)
    for line_a, line_b in zip(a.lines, b.lines):
        _assert_recipe_line(line_a, line_b)


def _assert_tech_map(a, b):
    """Call asserts for tech map"""
    assert type(a).__name__ == type(b).__name__
    assert a.name == b.name
    assert a.source == b.source
    assert a.general_manager == b.general_manager
    assert a.date_of_approval == b.date_of_approval
    _assert_organization(a.company, b.company)
    _assert_product(a.package, b.package)
    _assert_recipe(a.recipe, b.recipe)
    _assert_unit(a.unit, b.unit)