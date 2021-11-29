from abc import ABC, abstractmethod
from plistlib import Dict

from interface.Action import Action
from interface.Daimon import Daimon
from interface.Observation import Observation


class Agent(ABC):
    @abstractmethod
    def set_daimon(self, daimon: Daimon) -> None:
        pass

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def decide(self, observation: Observation) -> Action:
        pass

    @abstractmethod
    def distribute(self, observation: Observation) -> Dict[Action, float]:
        pass

    @abstractmethod
    def end(self, observation: Observation) -> None:
        pass
