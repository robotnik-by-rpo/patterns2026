"""Generate JSON dumps for PR review.

Run from project root:
    python -m scripts.dump_json
"""
import json
import os

from Src.Logics.convert_factory import convert_factory
from Src.Logics.storage_manager import storage_manager
from Src.Logics.settings_manager import setting_manager
from Src.Models.technical_map_model import technical_map_model


OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)),"Examples", "Json")


def dump(obj, filename: str) -> None:
    """Convert to JSON any object"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, filename)
    data = convert_factory().convert(obj)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2, default=str)
    print(f"saved: {path}")


def main() -> None:
    """Call save into JSON files"""
    manager = setting_manager()
    manager.load()
    dump(storage_manager(), "storage_manager.json")
    dump(technical_map_model.create_technical_map(), "technical_map.json")
    dump(manager.settings, "settings_snapshot.json")


if __name__ == "__main__":
    main()