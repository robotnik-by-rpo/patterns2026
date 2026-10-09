from Src.Models.recipe_model import recipe_model
from Src.Models.recipe_line_model import recipe_line_model
from Src.Models.ingredient_model import ingredient_model
from Src.Models.unit_of_measurement_model import unit_of_measurement_model


def test_recipe_exists():
    """Check recipe is created and has lines"""
    recipe = recipe_model.create_recipe()

    assert recipe is not None
    assert recipe.name == "French baguette"
    assert len(recipe.lines) >= 4


def test_recipe_has_instruction():
    """Check recipe has instruction steps"""
    recipe = recipe_model.create_recipe()
   
    assert len(recipe.instruction) > 0


def test_brutto_recipe_model():
    """Check brutto calculation"""
    recipe = recipe_model.create_recipe()
    brutto = recipe.brutto

    assert brutto > 0


def test_netto_recipe_model():
    """Check netto calculation"""
    recipe = recipe_model.create_recipe()
    netto = recipe.netto

    assert netto > 0
    assert netto <= recipe.brutto


def test_add_ingredient_recipe_model():
    """Check brutto grows after adding ingredient"""
    recipe = recipe_model.create_recipe()
    old_brutto = recipe.brutto
    g = unit_of_measurement_model.create_g()
    extra = ingredient_model("sugar", 10.0, 0, "brand", g)
    new_line = recipe_line_model(extra, 10.0, 1.0)
    recipe.lines.append(new_line)

    assert recipe.brutto == old_brutto + 10.0


def test_remove_ingredient_recipe_model():
    """Check brutto shrinks after removing ingredient"""
    recipe = recipe_model.create_recipe()
    old_brutto = recipe.brutto
    removed = recipe.lines[0]
    removed_brutto = removed.brutto
    recipe.lines.pop(0)

    assert recipe.brutto == old_brutto - removed_brutto