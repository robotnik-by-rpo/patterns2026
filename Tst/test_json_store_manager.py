import json
import pytest
from Src.Logics.convert_factory import convert_factory
from Src.Logics.storage_manager import storage_manager

def diff_dicts(a: any, b: any) -> bool:
    """Function for comparisons elements in dict"""
    if type(a) is not type(b):
        return False

    # Check equality dict
    if isinstance(a, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        for k in a.keys():
            if not diff_dicts(a[k], b[k]):
                return False
        return True

    # Check equality list
    if isinstance(a, list):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if not diff_dicts(a[i], b[i]):
                return False
        return True

    return a == b


@pytest.fixture(scope="module")
def factory() -> convert_factory:
    """Fixture of factory"""
    return convert_factory()


def test_storage_manager_to_json_to_dict(factory, tmp_path) -> None:
    """Check seriliazation and deseriliazation storage manager"""
    # Preparation
    manager = storage_manager()

    # Action
    original = factory.serialize(manager)

    assert isinstance(original, dict)
    assert original.get("__class__") == "storage_manager"

    target = tmp_path / "storage_manager.json"
    target.write_text(
        json.dumps(original, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    assert target.exists()

    loaded = json.loads(target.read_text(encoding="utf-8"))
    restored_obj: storage_manager = factory.deserialize(loaded)
    assert isinstance(restored_obj, storage_manager)
    restored = factory.serialize(restored_obj)             

    #Verification
    assert diff_dicts(original, restored)