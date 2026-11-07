from Src.Core.abstract_convert import abstract_convertor
from Src.Core.validate import validate
from datetime import datetime
from Src.Core.exception import arguments_exception

"""
Convertor for converting datetime
"""
class datetime_convertor(abstract_convertor):
    def convert(self, object: datetime) -> dict:
        """Convert datetime to iso format and split on parts"""
        return {"datetime": (validate.validated_type(object,
                                                     datetime,
                                                     "datetime", 
                                                     "wrong type, not datetime", 
                                                     arguments_exception)).isoformat(),
                "day": object.day,
                "month": object.month,
                "year": object.year,
                "hour": object.hour,
                "minute": object.minute,
                "second": object.second,
                "microsecond": object.microsecond}
