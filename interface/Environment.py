from abc import ABC, abstractmethod
from typing import List

from interface.Agent import Agent
from interface.Daimon import Daimon
from interface.History import History
from interface.Observation import Observation


class Environment(ABC):
    @abstractmethod
    def register(self, agent: Agent) -> None:
        pass

    @abstractmethod
    def construct_daimon(self) -> None:
        pass

    @abstractmethod
    def start_game(self) -> None:
        pass

    @abstractmethod
    def observe(self, history: History, agent: Agent) -> Observation:
        pass

    @abstractmethod
    def get_player_to_move(self, history: History) -> Agent:
        pass

    @abstractmethod
    def is_end(self, history: History) -> bool:
        pass

    @abstractmethod
    def get_possible_actions(self, history: History):
        pass

    @abstractmethod
    def get_agents(self) -> List[Agent]:
        pass

    @abstractmethod
    def get_daimons(self) -> List[Daimon]:
        pass
