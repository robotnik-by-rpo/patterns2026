from Src.Core.abc_data import unit
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
        self.__inn = self.__common_validated(inn, self._SIZE_INN, "INN")
        self.__bic = self.__common_validated(bic, self._SIZE_BIC, "BIC")
        self.__current_account = self.__common_validated(current_account, self._SIZE_CURRENT_ACCOUNT, "current account")
        self.__form_of_ownership = self.__validated_form_of_ownership(form_of_ownership)

    def __common_validated(self, unique_code: str, size: int, name_code:str) -> str:
        """Method for validating unique code, which have size"""
        if unique_code is not None:
            len_inn = len(unique_code)
            if (len_inn < size or len_inn > size):
                raise arguments_exception(name_code, f"{name_code} must have correct lenght")
        else: 
            raise arguments_exception(name_code, f"{name_code} must be exist")

        return unique_code   

    def __validated_form_of_ownership(self, form_of_ownership: str):
        """Method for validating"""
        if not self._EXIST_FORM_OF_OWNERSHIP.get(form_of_ownership,False):
            raise arguments_exception("form of ownership","form of ownership must be exist")
        return form_of_ownership
    
    @property
    def inn(self)->str:
        """Getting INN"""
        return self.__inn
    
    @inn.setter
    def inn(self, new_inn: str) -> None:
        """Setting INN"""
        self.__inn = self.__common_validated(new_inn, self._SIZE_INN,"INN")

    @property
    def bic(self)->str:
        """Getting BIC"""
        return self.__bic

    @bic.setter
    def bic(self, new_bic: str):
        """Setting BIC"""
        self.__bic = self.__common_validated(new_bic, self._SIZE_BIC,"BIC")

    @property
    def current_account(self) -> str:
        """Getting current account"""
        return self.__current_account

    @current_account.setter
    def current_account(self, new_current_account: str) -> None:
        """Setting current account"""
        self.__current_account = self.__common_validated(new_current_account, self._SIZE_CURRENT_ACCOUNT,"current account")

    @property
    def form_of_ownership(self) -> str:
        """Getting form of ownership"""
        return self.__form_of_ownership    
    
    @form_of_ownership.setter
    def form_of_ownership(self, new_form_of_ownership: str) -> None:
        """Setting form of ownership"""
        self.__form_of_ownership = self.__validated_form_of_ownership(new_form_of_ownership)