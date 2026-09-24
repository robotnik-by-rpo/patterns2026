class arguments_exception(Exception):
    __stack_trace: str = ""
    __msg: str = ""
    __field: str = ""

    def __init__(self, field, msg, stack_trace = ""):
        self.__msg = msg.strip()
        self.__stack_trace = stack_trace.strip()
        self.__field = field.strip()

    def __str__(self):
        return f"Error: Wrong argument {self.__field}\n{self.__msg}\n{self.__stack_trace}"