from tkinter import *
from FieldButton import FieldButton
from Ship import Ship
from ShipPlacement import ShipPlacement


class BotGame:
    def __init__(self, gui, variables):
        self.gui = gui
        self.field_size = int(variables[0].split()[0])
        self.ships_4 = variables[1]
        self.ships_3 = variables[2]
        self.ships_2 = variables[3]
        self.ships_1 = variables[4]
        self.player_ship_placement = ShipPlacement(gui, self.field_size, self.ships_4, self.ships_3,
                                                   self.ships_2, self.ships_1)
