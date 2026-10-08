from Src.Models.technical_map_model import technical_map_model
from Src.Models.organization_model import organization_model
from Src.Models.recipe_model import recipe_model
from Src.Models.ingredient_model import ingredient_model
from Src.Models.package_model import package_model
from datetime import datetime

def test_creating_technical_map_model():
    """Check creating technical map model"""
    tech = technical_map_model.create_technical_map()
    
    assert tech.company.name == organization_model.create_organization().name
    assert tech.recipe.name == recipe_model.create_recipe().name
    assert tech.name == "French baguette"
    assert tech.foodstuffs[0].name == ingredient_model.create_ingredients()[0].name
    assert tech.general_manager == "Lavrenov O.S."
    assert tech.source == "M. P. Mogilny 2nd edition DeLi plus, 2016, - 888 p."
    assert tech.package.name == package_model.create_package_paper().name
    assert tech.date_of_approval == datetime.strptime("08.09.25","%d.%m.%y")

def test_total_weight_dish_technical_map_model():
    """Check total weight of techical map"""
    tech = technical_map_model.create_technical_map()
    assert tech.total_weight == 344.0
