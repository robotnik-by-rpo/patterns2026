import csv
from io import StringIO
from Src.Models.technical_map_model import technical_map_model
from Src.Logics.csv_report import csv_report
from Src.Logics.md_report import md_report

def test_csv_report_binary_and_content():
    """Check decode csv report after encoding"""
    # preparation
    tech = technical_map_model.create_technical_map()

    # action
    result = csv_report().build(tech)

    # verification
    assert result.binary, "CSV must return binary"
    assert result.text == ""

    rows = list(csv.reader(StringIO(result.binary[0].decode("utf-8-sig"))))
    assert rows[0] == ["Code", "Name", "Brutto", "Netto"]
    assert len(rows) == 6
    assert "flour" in [r[1] for r in rows]


def test_md_report_binary_and_content():
    """Check decode markdown report after encoding"""
    # preparation
    tech = technical_map_model.create_technical_map()

    # action
    result = md_report().build(tech)

    # verification
    assert result.binary
    text = result.binary[0].decode("utf-8")
    assert text.startswith("| Code | Name |")
    assert "| flour |" in text