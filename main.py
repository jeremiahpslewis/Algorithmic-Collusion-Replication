"""
Replication of Artificial Intelligence, Algorithmic Pricing, and Collusion
    by: Calvano, Calzolari, Denicolò (2020)
    at: https://www.aeaweb.org/articles?id=10.1257/aer.20190623
Code
    author: Matteo Courthoud
    date: 07/05/2021
    git: https://github.com/matteocourthoud
    myself: https://matteocourthoud.github.io/
"""

from input.model import Algorithms
from input.qlearning import simulate_game

# Init algorithm
game = Algorithms()

# Compute equilibrium
game_equilibrium = simulate_game(game, 1e5, 1e7)
