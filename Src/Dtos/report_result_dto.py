from Src.Core.abc_data import unit
from Src.Core.validate import validate
from Src.Core.exception import arguments_exception

"""
    Модель для хранения результата отчета
"""
class report_result_dto(unit):
    __text: str = ""
    __binary: list[bytes] = []
 
    @property
    def text(self) -> str:
        return self.__text
    
    @property
    def binary(self) -> list[bytes]:
        return self.__binary
    

    @text.setter
    def text(self, new_text: str) -> None:
        new_text = validate.validated_null_value(new_text,
                            "new text",
                            "new text must be not value",
                            arguments_exception)
        self.__text = new_text
        self.__binary = []

    @binary.setter
    def binary(self, new_binary: list[bytes]) -> None:
        new_binary = validate.validated_null_value(new_binary,
                                                   "new binary",
                                                   "new binary must be not value",
                                                   arguments_exception)
        self.__text = ""
        self.__binary = new_binary