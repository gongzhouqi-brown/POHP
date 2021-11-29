from typing import List

from interface.Agent import Agent
from interface.Environment import Environment
from interface.History import History


def initiate_agents() -> List[Agent]:
    pass


def initiate_environment() -> Environment:
    pass


T = 10000
agents = initiate_agents()
G = initiate_environment()
for M in agents:
    G.register(M)
G.construct_daimon()
for M, D in zip(G.get_agents(), G.get_daimons()):
    M.set_daimon(D)
for i in range(T):
    H = History()
    for M in G.get_agents():
        M.start()
    M = G.get_player_to_move(H)
    while not G.is_end(H):
        a = M.decide(G.observe(H, M))
        H.append(a)
    for M in G.get_agents():
        M.end(G.observe(H, M))
