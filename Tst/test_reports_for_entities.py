import pytest
from Src.Models.technical_map_model import technical_map_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model
from Src.Models.group_nomenclature_model import group_nomenclature_model
from Src.Logics.text_report import text_report
from Src.Logics.report_helper import extract_table


@pytest.fixture
def flour_nomenclature():
    group = group_nomenclature_model("ingredients")
    noms = nomenclature_model.create_crude_ingredients(
        group, unit_of_measurement_model.create_kg())
    return noms["flour"]


def test_tech_map_extract_returns_recipe_table():
    """Check headers and rows from recipe"""
    # preparation
    tech = technical_map_model.create_technical_map()

    # action
    header, rows = extract_table(tech)

    # verification
    assert header == ["Code", "Name", "Brutto", "Netto"]
    assert len(rows) == 5


def test_nomenclature_extract_returns_field_table(flour_nomenclature):
    """Check headers from nomenclature"""
    # preparation

    # action
    header, rows = extract_table(flour_nomenclature)

    # verification
    assert header == ["Code", "Name", "Full name", "Group", "Base unit", "Type"]
    assert len(rows) == 1

    row = rows[0]
    assert row[1] == "flour"
    assert row[2] == "flour MAKFA"
    assert row[3] == "ingredients"    
    assert row[4] == "kilogram"
    assert row[5] == "crude"      


def test_unit_extract_returns_field_table():
    """Check headers from unit of measurement"""
    # preparation
    gram = unit_of_measurement_model.create_g()

    # action
    header, rows = extract_table(gram)

    # verification
    assert header == ["Code", "Name", "Coef", "Base"]
    assert len(rows) == 1
    row = rows[0]
    assert row[1] == "gram"
    assert row[2] == 1
    assert row[3] == "" 


def test_text_report_for_nomenclature(flour_nomenclature):
    # preparation
    report = text_report()

    # action
    result = report.build(flour_nomenclature)

    # verification
    assert "Code | Name | Full name | Group | Base unit | Type" in result.text
    assert "flour" in result.text
    assert "flour MAKFA" in result.text
    assert "ingredients" in result.text