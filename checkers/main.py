"""
@Author: Erwin de Wolff

Main file for checkers

"""

from game import *
from window import *

""" Main loop to let two players play checkers against each other """

# Set game and players
game = Game(rows=8, columns=8)

# Start view/controller
window = GameWindow(game)
