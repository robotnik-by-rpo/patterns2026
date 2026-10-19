import pytest
from Src.Logics.report_factory import report_factory
from Src.Dtos.report_type_dto import report_type_enum
from Src.Core.exception import arguments_exception
from Src.Models.technical_map_model import technical_map_model
from Src.Logics.text_report import text_report
from enum import Enum

class _UnknownReportType(Enum):
    """Value, which don't have in __mapping"""
    UNKNOWN = 999

def test_succefful_mapping_report_factory():
    #preparaion
    rep = report_factory().create(report_type_enum.TXT)

    #action

    #verification
    assert rep is not None

def test_fault_mapping_report_factory():
    #preparaion
    rep = report_factory()
    
    #action
    with pytest.raises(arguments_exception) as exception:
        _ = rep.create(_UnknownReportType)
   
    #verification
    assert "Wrong argument" in str(exception.value)
    assert "report type" in str(exception.value)

def test_get_text_report_from_report_factory():
    #preparation
    factory = report_factory()
    tech = technical_map_model.create_technical_map()

    #action
    report = factory.create(report_type_enum.TXT)
    result = report.build(tech)

    #verification
    assert report is not None
    assert isinstance(report, text_report)
    assert result is not None
    assert "Code | Name" in result.text
    assert "flour" in result.text