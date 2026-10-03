from Src.Logics.settings_manager import setting_manager
from Src.Core.exception import operation_exception

def test_not_raise_settings_manager_load():
    """Check loading file"""
    #Preparing
    manager  = setting_manager()
    try:
        manager.load()
        assert True
    except operation_exception:
        assert False
    except:
        assert False


def test_not_none_settings_manager_load():
    """Check settings aren't None"""
    #Preparing
    manager  = setting_manager()
    try:
        manager.load()
        assert True
    except operation_exception:
        assert False
    except:
        assert False

    assert manager.settings is not None


def test_equals_settings_manager_create():
    """Check equals between objects"""
    instance1 = setting_manager()
    instance2 = setting_manager()

    assert instance1 == instance2 

def test_is_loaded_settings_manager_true():
    """Check flag is_loaded after uploading file"""
    manager = setting_manager()
    try:
        manager.load()
    except:
        assert False

    assert manager.is_loaded

def test_settings_manager_settings_filled_after_load():
    """Check settings are filled with data after uploading file"""
    manager = setting_manager()
    try:
        manager.load()
    except operation_exception:
        assert False

    assert manager.settings.company is not None
    assert manager.settings.boss_name != ""
    assert manager.settings.accounter_name != ""

def test_settings_manager_equals_json():
    """Check equals between attributes and key value from json file"""
    manager = setting_manager()
    manager.load()
    assert manager.settings.boss_name == "boss"
    assert manager.settings.accounter_name == "accounter"
    assert manager.settings.company.inn == "1829111559"
    assert manager.settings.company.bic == "124125513"
    assert manager.settings.company.current_account == "18291112593229111559"
    assert manager.settings.company.form_of_ownership == "ООО"
    assert manager.settings.company.name == "Ромашка"

    assert manager.settings.is_first == True