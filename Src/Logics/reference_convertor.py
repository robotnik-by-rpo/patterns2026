import inspect
from Src.Core.abstract_convert import abstract_convertor
from Src.Core.exception import not_exist_exception
from Src.Logics.classes_registry import classes_registry

"""
Class for collecting fields of non-basic and non-datetime objects
"""
class reference_convertor(abstract_convertor):
    def serialize(self, obj: any) -> dict:
        """Method for checking type object and returning fields"""
        if not hasattr(obj, "__dict__") or callable(obj):
            raise not_exist_exception(
                "type of object", f"unsupported type: {type(obj).__name__}",
            )

        names: set[str] = set()
        for name in vars(obj):
            if not name.startswith("_"):
                names.add(name)
        for name, member in inspect.getmembers(type(obj)):
            if isinstance(member, property) and not name.startswith("_"):
                names.add(name)

        fields: dict = {"__class__": type(obj).__name__}
        for name in names:
            try:
                value = getattr(obj, name)
            except Exception:
                continue
            if callable(value):
                continue
            fields[name] = value     
        return fields
    
    def deserialize(self, data: dict) -> any:
        "Method for deserialization"
        type_name = data["__class__"]
        cls = classes_registry().get(type_name)
        if cls is None:
            raise not_exist_exception("__class__", f"undefine class {type_name}")


        instance = cls.__new__(cls)
        fields = {k: v for k, v in data.items() if k != "__class__"}

        self.__assign(instance, fields)
        return instance

    @staticmethod
    def __assign(obj: any, data: dict) -> None:
        """Method for getting attributes for object"""
        prefix = f"_{type(obj).__name__}__"
        private_attr = {
            name[len(prefix):]: name
            for name in vars(obj)
            if name.startswith(prefix)
        }

        for key, value  in data.items():
            prop = getattr(type(obj), key, None)
            if isinstance(getattr(type(obj), key, None), property):
                if prop.fset is not None:
                    try:
                        setattr(obj, key, value)
                        continue
                    except Exception:
                        ...
                continue

            if key in private_attr:
                setattr(obj, private_attr[key], value)
                continue

            setattr(obj, key, value)

    def can_serialize(self, obj: any) -> bool:
        """Method for check possibility for serialize"""
        return (
            hasattr(obj, "__dict__")
            and not callable(obj)
            and not isinstance(obj, (bool, int, float, str))
        )

    def can_deserialize(self, data: any) -> bool:
        """Method for check possibility for deserialize"""
        return isinstance(data, dict) and "__class__" in data