from Src.Core.abc_data import unit

class group_nomenclature_model(unit):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    @classmethod
    def create_groups(cls) -> dict[str,"group_nomenclature_model"]:
        "Factory method for creating groups of nomenclature"
        groups = {}
        name_groups = ["order", 
                       "ingredients", 
                       "blanks",
                       "prepack",
                       "finished products",
                       "consumables"]

        for n in name_groups:
            groups[n]=group_nomenclature_model(n)
        return groups
