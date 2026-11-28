from Src.Core.abstract_observation import abstract_observation

"""
Class observer for event tracking
"""
class observer:
    # list observers
    handlers: list[abstract_observation] = []


    @staticmethod
    def add(source: abstract_observation) -> None:
        """Method for signing object"""
        for handler in observer.handlers:
            if handler == source:
                return        
        observer.handlers.append(source)

    @staticmethod
    def delete(source: abstract_observation) -> None:
        """Method for unsubscribing object"""
        for handler in observer.handlers:
            if handler == source:
                observer.handlers.remove(handler)


    @staticmethod
    def create (event_types: str, params: object | None = None) -> None:
        """Method for public event all subscribers"""
        for handler in observer.handlers:
            if handler is not None:
                handler.handler(event_types, params)    