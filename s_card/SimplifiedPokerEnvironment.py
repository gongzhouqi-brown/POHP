from typing import List

from interface.Agent import Agent
from interface.Daimon import Daimon
from interface.Environment import Environment
from interface.History import History
from interface.Observation import Observation


class SimplifiedPokerEnvironment(Environment):
    def __init__(self):
        self.players = []
        self.now_registered = 0
        self.min_players = 2
        self.max_players = 2

    def register(self, agent: Agent) -> None:
        assert self.now_registered < self.max_players
        self.players.append(agent)
        self.now_registered += 1

    def construct_daimon(self) -> None:
        pass

    def start_game(self) -> None:
        pass

    def observe(self, history: History, agent: Agent) -> Observation:
        pass

    def get_player_to_move(self, history: History) -> Agent:
        pass

    def is_end(self, history: History) -> bool:
        pass

    def get_possible_actions(self, history: History):
        pass

    def get_agents(self) -> List[Agent]:
        pass

    def get_daimons(self) -> List[Daimon]:
        pass