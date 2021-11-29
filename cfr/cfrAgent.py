from plistlib import Dict

from interface.Action import Action
from interface.Agent import Agent
from interface.Daimon import Daimon
from interface.Observation import Observation


class cfrAgent(Agent):
    def __init__(self):
        pass

    def set_daimon(self, daimon: Daimon) -> None:
        pass

    def start(self) -> None:
        pass

    def decide(self, observation: Observation) -> Action:
        pass

    def distribute(self, observation: Observation) -> Dict[Action, float]:
        pass

    def end(self, observation: Observation) -> None:
        pass
