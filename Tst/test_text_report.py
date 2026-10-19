import pytest 
from Src.Models.technical_map_model import technical_map_model
from Src.Logics.text_report import text_report
from Src.Core.exception import arguments_exception

def test_creating_tech_map_of_text_report():
    """Check techical map text"""
    #Preparation
    tech = technical_map_model.create_technical_map()
    
    #Action
    report = text_report().build(tech)

    #Verification
    assert report is not None
    assert "Code | Name" in report.text
    assert "flour" in report.text

def test_text_report_rejects_non_unit():
    """Check wrong data"""
    #Preparation

    #Action
    with pytest.raises(arguments_exception) as exception:
        _ = text_report().build({"not": "a unit"})

    # verification
    assert "Wrong argument" in str(exception.value)
    assert "source" in str(exception.value)