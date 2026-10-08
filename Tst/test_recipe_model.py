from Src.Models.recipe_model import recipe_model

def test_create_recipe_model():
    """Check create new recipe"""
    recipe = recipe_model.create_recipe()
    assert recipe.name == "French baguette"

def test_name_setter_recipe_model():
    """Check name setter of recipe"""
    recipe = recipe_model.create_recipe()
    new_name = "Homemade bun"
    recipe.name = new_name
    assert recipe.name == new_name

def test_recipe_setter_recipe_model():
    """Check recipe setter of recipe"""
    recipe = recipe_model.create_recipe()
    new_recipe = ["First step","Second step","Third step"]
    recipe.recipe = new_recipe
    assert recipe.recipe == new_recipe