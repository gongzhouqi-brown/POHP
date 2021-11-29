from abc import ABC, abstractmethod
from typing import Dict

from interface.Action import Action
from interface.History import History


class Daimon(ABC):
    @abstractmethod
    def sample(self, history: History) -> Action:
        pass

    @abstractmethod
    def distribute(self, history: History) -> Dict[Action, float]:
        pass
