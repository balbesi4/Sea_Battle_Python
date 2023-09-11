from FieldButton import FieldButton
from Ship import Ship
from tkinter import *


class ShipPlacement:
    def __init__(self, gui, field_size, ships_4, ships_3, ships_2, ships_1):
        self.gui = gui
        self.field_size = field_size
        self.ships = [4 for _ in range(ships_4)] + [3 for _ in range(ships_3)] + \
                     [2 for _ in range(ships_2)] + [1 for _ in range(ships_1)]
        self.field = []
        self.game_window = None
        self.ship_colors = ["black", "#064020", "#AA0020", "#22DDCC", "#888888", "#70AA00",
                            "#1111CC", "#FFFF66", "#FFB266", "#B266FF", "#663300"]
        self.place_ships()

    def place_ships(self):
        # создание разметки для поля size x size

        self.game_window = Toplevel(self.gui.window)
        self.game_window.resizable(0, 0)
        self.game_window.grab_set()
        self.game_window.geometry(f"{self.field_size * 50 + 200}x{self.field_size * 50 + 50}")

        letters = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "К", "Л"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]

        field_label = Label(self.game_window, text="Расставьте ваши корабли", font=("Roboto", 16))
        field_label.grid(row=0, column=0, columnspan=self.field_size + 1, pady=10)

        for k in range(self.field_size):
            number_label = Label(self.game_window, text=numbers[k])
            number_label.grid(row=k + 2, column=0, padx=10)
            letter_label = Label(self.game_window, text=letters[k])
            letter_label.grid(row=1, column=k + 1, pady=10)

        # создание игрового поля и отрисовка кораблей

        next_ship_cord = (0, 0)
        current_ship_index = 0
        current_len = 0
        ship = Ship(self.ships[0], "h", self.ship_colors[0], (0, 0))
        for i in range(self.field_size):
            self.field.append([])
            for j in range(self.field_size):
                if next_ship_cord == (j, i) and current_ship_index < len(self.ships) and current_len < self.ships[current_ship_index]:
                    self.field[i].append(FieldButton(self.game_window, ship, i, j))
                    current_len += 1
                    if current_len + 1 > self.ships[current_ship_index]:
                        next_ship_cord = (next_ship_cord[0] + 2, next_ship_cord[1]) if next_ship_cord[0] + 2 < self.field_size else (0, next_ship_cord[1] + 2)
                    else:
                        next_ship_cord = (next_ship_cord[0] + 1, next_ship_cord[1])
                else:
                    self.field[i].append(FieldButton(self.game_window, None, i, j))
                    if current_len != 0:
                        current_ship_index += 1
                        if current_ship_index < len(self.ships):
                            ship = Ship(self.ships[current_ship_index], "h", self.ship_colors[current_ship_index], next_ship_cord)
                    current_len = 0
