from Src.Core.abc_data import unit
from Src.Models.technical_map_model import technical_map_model


def extract_table(source: unit) -> tuple[list[str], list[list]]:
    """
    Return (header, rows) for some object of unit.
    For technical map — lines recipe. For other — field of object.
    """
    if isinstance(source, technical_map_model):
        header = ["Code", "Name", "Brutto", "Netto"]
        rows = [
            [line.component.id, line.component.name,
             line.component.brutto, line.component.netto]
            for line in source.recipe.lines
        ]
        return header, rows

    header = ["Field", "Value"]
    rows = []
    for key, value in vars(source).items():
        clean = key.split("__")[-1] if key.startswith("_") else key
        if isinstance(value, (str, int, float, bool)) or value is None:
            rows.append([clean, value])
        else:
            rows.append([clean, repr(value)])
    return header, rows