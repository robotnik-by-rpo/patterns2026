from Src.Core.abc_data import unit
from Src.Core.validate import validate
from Src.Core.exception import arguments_exception

class organization_model(unit):
    """It's class for initing organization model"""
    _SIZE_INN: int = 10
    _SIZE_BIC: int = 9
    _SIZE_CURRENT_ACCOUNT: int = 20
    _EXIST_FORM_OF_OWNERSHIP: dict[str, bool] = {"ИП":True,
                                                  "ООО":True,
                                                  "АО":True,
                                                  "НКО":True}
    __inn: str
    __bic: str
    __current_account: str
    __form_of_ownership: str

    def __init__(self, 
                 name:str, 
                 inn: str,
                 bic: str, 
                 current_account: str,
                 form_of_ownership: str):
        super().__init__()
        self.name = name
        self.__inn = validate.validated_certain_size(inn, 
                                                     self._SIZE_INN, 
                                                     "INN",
                                                     arguments_exception)
        self.__bic = validate.validated_certain_size(bic, 
                                                     self._SIZE_BIC, 
                                                     "BIC",
                                                     arguments_exception)
        self.__current_account = validate.validated_certain_size(current_account, 
                                                                 self._SIZE_CURRENT_ACCOUNT, 
                                                                 "current account",
                                                                 arguments_exception)
        self.__form_of_ownership = validate.validated_value_exist(form_of_ownership,
                                                                  self._EXIST_FORM_OF_OWNERSHIP,
                                                                  "form of ownership",
                                                                  "form of ownership must be exist",
                                                                  arguments_exception)
        
    @property
    def inn(self)->str:
        """Getting INN"""
        return self.__inn
    
    @inn.setter
    def inn(self, new_inn: str) -> None:
        """Setting INN"""
        self.__inn = validate.validated_certain_size(new_inn, 
                                                     self._SIZE_INN, 
                                                     "INN",
                                                     arguments_exception)

    @property
    def bic(self)->str:
        """Getting BIC"""
        return self.__bic

    @bic.setter
    def bic(self, new_bic: str):
        """Setting BIC"""
        self.__bic = validate.validated_certain_size(new_bic, 
                                                     self._SIZE_BIC, 
                                                     "BIC",
                                                     arguments_exception)

    @property
    def current_account(self) -> str:
        """Getting current account"""
        return self.__current_account

    @current_account.setter
    def current_account(self, new_current_account: str) -> None:
        """Setting current account"""
        self.__current_account = validate.validated_certain_size(new_current_account, 
                                                                 self._SIZE_CURRENT_ACCOUNT, 
                                                                 "current account",
                                                                 arguments_exception)
    @property
    def form_of_ownership(self) -> str:
        """Getting form of ownership"""
        return self.__form_of_ownership    
    
    @form_of_ownership.setter
    def form_of_ownership(self, new_form_of_ownership: str) -> None:
        """Setting form of ownership"""
        self.__form_of_ownership = validate.validated_value_exist(new_form_of_ownership,
                                                                  self._EXIST_FORM_OF_OWNERSHIP,
                                                                  "form of ownership",
                                                                  "form of ownership must be exist",
                                                                  arguments_exception)
         
    @classmethod
    def create_organization(cls) -> "organization_model":
        return cls("Ромашка",
                    "1350791749",
                    "782189947",
                    "78328490185897461647",
                    "ООО")