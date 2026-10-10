from datetime import datetime
from Src.Models.technical_map_model import technical_map_model
from Src.Models.recipe_model import recipe_model
from Src.Models.recipe_line_model import recipe_line_model
from Src.Models.organization_model import organization_model
from Src.Models.package_model import package_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model


def _make_lunch(baguette, share: float) -> technical_map_model:
    """Supported factory function: lunch with share of baguette"""
    return technical_map_model(
        "Business lunch",
        recipe_model("Business lunch recipe", [
            recipe_line_model(baguette, 1.0, share)
        ]),
        "internal",
        datetime.now(),
        "Ivanov I.I.",
        organization_model.create_organization(),
        package_model.create_package_paper(),
        unit_of_measurement_model.create_g()
    )


def test_brutto_technical_map_model():
    """Check brutto of technical map equals sum of recipe lines"""
    # preparation
    tech = technical_map_model.create_technical_map()
    brutto = tech.brutto
    expected = sum(line.brutto for line in tech.recipe.lines)

    #action

    # verification
    assert brutto == expected


def test_netto_technical_map_model():
    """Check netto of technical map equals sum of recipe lines"""
    # preparation
    tech = technical_map_model.create_technical_map()
    netto = tech.netto
    expected = sum(line.netto for line in tech.recipe.lines)

    #action

    # verification
    assert netto == expected


def test_waste_default_technical_map_model():
    """Check waste stays default (0.0)"""
    # preparation
    tech = technical_map_model.create_technical_map()
    waste = tech.waste

    #action

    # verification
    assert waste == 0.0


def test_recursive_brutto_technical_map_model():
    """Check recursive brutto: dish inside dish"""
    # preparation
    baguette = technical_map_model.create_technical_map()
    lunch = _make_lunch(baguette, 0.5)
    brutto = lunch.brutto
    expected = baguette.brutto * 0.5

    #action

    # verification
    assert brutto == expected


def test_recursive_netto_technical_map_model():
    """Check recursive netto: dish inside dish"""
    # preparation
    baguette = technical_map_model.create_technical_map()
    lunch = _make_lunch(baguette, 0.25)
    netto = lunch.netto
    expected = baguette.netto * 0.25

    #action

    # verification
    assert netto == expected


def test_recursive_technical_map_in_technical_map():
    """Check recursion depth 2: tech map inside tech map"""
    # preparation
    baguette = technical_map_model.create_technical_map()
    lunch = _make_lunch(baguette, 0.5)
    dinner = _make_lunch(lunch, 0.5)

    # action
    brutto = dinner.brutto
    netto = dinner.netto

    # verification
    assert brutto == baguette.brutto * 0.25
    assert netto == baguette.netto * 0.25