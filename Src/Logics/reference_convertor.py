import inspect
from Src.Core.abstract_convert import abstract_convertor
from Src.Core.exception import not_exist_exception

"""
Class for collecting fields of non-basic and non-datetime objects
"""
class reference_convertor(abstract_convertor):
    def convert(self, obj: any) -> dict:
        """Method for checking type object and returning fields"""
        if not hasattr(obj, "__dict__") or callable(obj):
            raise not_exist_exception(
                "type of object",
                f"unsupported type: {type(obj).__name__}",
            )
        return self.__collect_fields(obj)

    def __collect_fields(self, obj: any) -> dict:
        """Method for collecting fields"""
        names: set[str] = set()
        for name in vars(obj):
            if not name.startswith("_"):
                names.add(name)
        for name, member in inspect.getmembers(type(obj)):
            if isinstance(member, property) and not name.startswith("_"):
                names.add(name)

        fields: dict = {}
        for name in names:
            try:
                value = getattr(obj, name)
            except Exception:
                continue
            if callable(value):
                continue
            fields[name] = value
        return fields