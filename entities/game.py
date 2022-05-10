import json
import os
from entities.properties import Monopoly, Property


class Game:
    def __init__(self, players_number):
        self.players_number = players_number

