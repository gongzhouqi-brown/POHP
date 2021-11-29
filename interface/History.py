from abc import ABC, abstractmethod

from interface.Action import Action


class History(ABC):
    @abstractmethod
    def append(self, action: Action) -> None:
        pass
