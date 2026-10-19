from Src.Models.technical_map_model import technical_map_model
from Src.Logics.xml_report import xml_report
from Src.Logics.html_report import html_report

def test_xml_report_structure():
    """Check structure of xml report"""
    # preparation
    tech = technical_map_model.create_technical_map()

    # action
    result = xml_report().build(tech)
    
    # verification
    assert result.text.startswith("<?xml")
    assert result.text.rstrip().endswith("</report>")
    assert result.text.count("<row ") == 5
    assert 'name="flour"' in result.text


def test_html_report_structure():
    """Check structure of html report"""
    # preparation
    tech = technical_map_model.create_technical_map()

    # action
    result = html_report().build(tech)
    
    # verification
    assert "<table" in result.text
    assert "</table>" in result.text
    assert result.text.count("<tr>") == 6
    assert "flour" in result.text