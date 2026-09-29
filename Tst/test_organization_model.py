from Src.Models.organization_model import organization_model
from Src.Core.exception import arguments_exception
import pytest

def test_organization_model_name_initing():
    """Check name after initing"""
    org = organization_model("Ромашка","1"*10,"1"*9,"1"*20,"ООО")
    assert org.name == "Ромашка"

def test_organization_model_inn_initing():
    """Check inn after initing"""
    org = organization_model("Ромашка","1"*10,"1"*9,"1"*20,"ООО")
    assert org.inn == "1"*10

def test_organization_model_bic_initing():
    """Check bic after initing"""
    org = organization_model("Ромашка","1"*10,"1"*9,"1"*20,"ООО")
    assert org.bic == "1"*9

def test_organization_model_current_account_initing():
    """Check current account after initing"""
    org = organization_model("Ромашка","1"*10,"1"*9,"1"*20,"ООО")
    assert org.current_account == "1"*20

def test_organization_model_form_of_ownership_initing():
    """Check from of ownership after initing"""
    org = organization_model("Ромашка","1"*10,"1"*9,"1"*20,"ООО")
    assert org.form_of_ownership == "ООО"


def test_organization_model_null_name():
    """Check name on None value"""
    with pytest.raises(arguments_exception) as exception:
        _ = organization_model(None,"1"*10,"1"*9,"1"*20,"ООО")
    
    assert "Wrong argument" in str(exception.value)
    assert "name" in str(exception.value)

def test_organization_model_null_inn():
    """Check inn on None value"""
    with pytest.raises(arguments_exception) as exception:
        _ = organization_model("Ромашка",None,"1"*9,"1"*20,"ООО")
    
    assert "Wrong argument" in str(exception.value)
    assert "INN" in str(exception.value)

def test_organization_model_null_bic():
    """Check bic on None value"""
    with pytest.raises(arguments_exception) as exception:
        _ = organization_model("Ромашка","1"*10,None,"1"*20,"ООО")
    
    assert "Wrong argument" in str(exception.value)
    assert "BIC" in str(exception.value)

def test_organization_model_null_current_account():
    """Check current account on None value"""
    with pytest.raises(arguments_exception) as exception:
        _ = organization_model("Ромашка","1"*10,"1"*9,None,"ООО")
    
    assert "Wrong argument" in str(exception.value)
    assert "current account" in str(exception.value)

def test_organization_model_null_form_of_ownership():
    """Check form of ownership on None value"""
    with pytest.raises(arguments_exception) as exception:
        _ = organization_model("Ромашка","1"*10,"1"*9,"1"*20,None)
    
    assert "Wrong argument" in str(exception.value)
    assert "form of ownership" in str(exception.value)

def test_organization_model_name_setter():
    """Check name setter on value after setting"""
    org = organization_model("Ромашка","1"*10,"1"*9,"1"*20,"ООО")
    org.name = "Ромашка 1"
    assert org.name == "Ромашка 1"

def test_organization_model_inn_setter():
    """Check inn setter on value after setting"""
    org = organization_model("Ромашка","1"*10,"1"*9,"1"*20,"ООО")
    org.inn = '2'*10
    assert org.inn == "2"*10

def test_organization_model_bic_setter():
    """Check bic setter on value after setting"""
    org = organization_model("Ромашка","1"*10,"1"*9,"1"*20,"ООО")
    org.bic = '2'*9
    assert org.bic == '2'*9

def test_organization_model_current_account_setter():
    """Check current_account setter on value after setting"""
    org = organization_model("Ромашка","1"*10,"1"*9,"1"*20,"ООО")
    org.current_account = '2'*20
    assert org.current_account == '2'*20

def test_organization_model_empty_form_of_ownership_setter():
    """Check form of ownership setter on value after setting"""
    org = organization_model("Ромашка","1"*10,"1"*9,"1"*20,"ООО")
    org.form_of_ownership = "ИП"
    assert org.form_of_ownership == "ИП"


def test_organization_model_inn_limit_longer():
    """Check inn on lenght if lenght longer than 10"""
    with pytest.raises(arguments_exception) as exception:
        _ = organization_model("Ромашка","1"*11,"1"*9,"1"*20,"ООО")
    
    assert "Wrong argument" in str(exception.value)
    assert "INN" in str(exception.value)

def test_organization_model_bic_limit_longer():
    """Check bic on lenght if lenght longer than 9"""
    with pytest.raises(arguments_exception) as exception:
        _ = organization_model("Ромашка","1"*10,"1"*10,"1"*20,"ООО")
    
    assert "Wrong argument" in str(exception.value)
    assert "BIC" in str(exception.value)
def test_organization_model_current_account_limit_longer():
    """Check current account on lenght if lenght longer than 20"""
    with pytest.raises(arguments_exception) as exception:
        _ = organization_model("Ромашка","1"*10,"1"*9,'1'*21,"ООО")
    
    assert "Wrong argument" in str(exception.value)
    assert "current account" in str(exception.value)


def test_organization_model_inn_limit_shorter():
    """Check inn on lenght if lenght shorter than 10"""
    with pytest.raises(arguments_exception) as exception:
        _ = organization_model("Ромашка",'1'*9,"1"*9,"1"*20,"ООО")
    
    assert "Wrong argument" in str(exception.value)
    assert "INN" in str(exception.value)

def test_organization_model_bic_limit_shorter():
    """Check bic on lenght if lenght shorter than 9"""
    with pytest.raises(arguments_exception) as exception:
        _ = organization_model("Ромашка","1"*10,"1"*8,"1"*20,"ООО")
    
    assert "Wrong argument" in str(exception.value)
    assert "BIC" in str(exception.value)

def test_organization_model_current_account_limit_shorter():
    """Check current account on lenght if lenght shorter than 20"""
    with pytest.raises(arguments_exception) as exception:
        _ = organization_model("Ромашка","1"*10,"1"*9,"1"*19,"ООО")
    
    assert "Wrong argument" in str(exception.value)
    assert "current account" in str(exception.value)


def test_organization_model_undefine_form_of_ownership():
    """Check form of ownership on existing kinds"""
    with pytest.raises(arguments_exception) as exception:
        _ = organization_model("Ромашка","1"*10,"1"*9,"1"*20,"ОИП")
    
    assert "Wrong argument" in str(exception.value)
    assert "form of ownership" in str(exception.value)
