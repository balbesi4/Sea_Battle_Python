from tkinter import *


class FieldButton:
    def __init__(self, game_window, ship, x, y):
        self.ship = ship
        self.x = x
        self.y = y
        self.game_window = game_window
        color = "white" if ship is None else ship.color
        self.button = Button(game_window, bg=color, height=2, width=4, activebackground=color)
        self.button.grid(row=x + 2, column=y + 1)

    def toggle(self):
        pass

    def set_ship_color(self, ship):
        pass
