class arguments_exception(Exception):
    """class for args errors"""
    __stack_trace: str = ""
    __msg: str = ""
    __field: str = ""

    def __init__(self, field: str, msg: str, stack_trace: str = ""):
        self.__msg = str(msg).strip()
        self.__stack_trace = str(stack_trace).strip()
        self.__field = str(field).strip()

    @property
    def field(self) -> str:
        """Getter for field"""
        return self.__field

    @property
    def msg(self) -> str:
        """Getter for msg"""
        return self.__msg

    @property
    def stack_trace(self) -> str:
        """Getter for stack trace"""
        return self.__stack_trace

    def __str__(self):
        return f"Error: Wrong argument {self.field}\n{self.msg}\n{self.stack_trace}"
    
class operation_exception(arguments_exception):
    """class for operation errors"""
    def __str__(self):
        return f"Error: Wrong operation {self.field}\n{self.msg}\n{self.stack_trace}"
    
class not_exist_exception(arguments_exception):
    """class for not exist erros"""
    def __str__(self):
        return f"Error: It doesn't exist {self.field}\n{self.msg}\n{self.stack_trace}"