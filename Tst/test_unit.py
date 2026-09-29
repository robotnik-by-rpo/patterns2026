# Необходимо установить pip install pytest в терминале с подключенным Environment
# Далее, настройки
# {
#    "python.testing.pytestArgs": [
#        "Tst"
#    ],
#    "python.testing.unittestEnabled": false,
#    "python.testing.pytestEnabled": true
#}

from Src.Core.abc_data import unit
from Src.Core.exception import arguments_exception
import pytest


# тестовая сущность
class test_unit(unit):
    pass

def test_unit_id_not_null():
    """After init model his uuid not empty"""
    # Подготовака
    entity = test_unit()
    result = entity.id

    assert result != ""

def test_unit_unique():
    """Two created models get other unique uuid"""
    entity1 = test_unit()
    entity2 = test_unit()

    assert entity1.id != entity2.id


def test_unit_two_work():
    """After getting the same uuid for two models, they must be the same"""
    entity1 = test_unit()
    entity2 = test_unit()

    entity1.id = "fff"
    entity2.id = "fff"

    assert entity2.id == entity1.id

def test_argument_exception_witn_empty_name():
    entity = test_unit()
    empty_name = ""

    with pytest.raises(arguments_exception) as exception:
        entity.name = empty_name
    
    assert "Wrong argument" in str(exception.value)
    assert "Empty name" in str(exception.value)

# Пример простого теста
def test_start():
    assert 1 == 1