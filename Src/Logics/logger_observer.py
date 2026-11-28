from datetime import datetime
from Src.Core.abstract_observation import abstract_observation
from Src.Logics.observer import observer

class logger_observer(abstract_observation):
    __save_file: str = ""

    def __init__(self, user_save_file: str = "services.log"):
        self.__save_file = user_save_file
        observer.add(self)

    def handler(self, event_types: str, params: object):
        dt = datetime.now().isoformat()
        info = f"[{dt}]\tevent={event_types}\tparams={params}"
        print(info)
        with open(self.__save_file, "a", encoding="utf-8") as file:
            file.write(info+"\n")