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
    assert header == ["Field", "Value"]
    keys = [r[0] for r in rows]
    assert "name" in keys
    assert "coef" not in keys     


def test_unit_extract_returns_field_table():
    """Check headers from unit of measurement"""
    # preparation
    gram = unit_of_measurement_model.create_g()

    # action
    header, rows = extract_table(gram)

    # verification
    assert header == ["Field", "Value"]
    keys = [r[0] for r in rows]
    assert "coef" in keys


def test_text_report_for_nomenclature(flour_nomenclature):
    # preparation
    report = text_report()

    # action
    result = report.build(flour_nomenclature)

    # verification
    assert "Field" in result.text
    assert "flour" in result.text