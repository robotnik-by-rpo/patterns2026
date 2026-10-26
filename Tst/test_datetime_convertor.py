import pytest
from datetime import datetime
from Src.Logics.datetime_convertor import datetime_convertor

def test_datetime_convertor_converts_datetime():
    """Check datetime -> dict with iso and parts"""
    # Preparation
    convertor = datetime_convertor()
    value = datetime(2025, 9, 8, 14, 30, 15)

    # Action
    result = convertor.convert(value)

    # Verification
    assert result["datetime"] == value.isoformat()
    assert result["day"] == 8
    assert result["month"] == 9
    assert result["year"] == 2025
    assert result["hour"] == 14
    assert result["minute"] == 30
    assert result["second"] == 15


def test_datetime_convertor_rejects_not_datetime():
    """Check non-datetime raises"""
    # Preparation
    convertor = datetime_convertor()

    # Action
    with pytest.raises(Exception) as exception:
        _ = convertor.convert("2025-09-08")

    # Verification
    assert "datetime" in str(exception.value) or "type" in str(exception.value)