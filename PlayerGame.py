from tkinter import *


class PlayerGame:
    def __init__(self, gui, variables):
        self.gui = gui
        self.field_size = variables[0]
        self.ships_4 = variables[1]
        self.ships_3 = variables[2]
        self.ships_2 = variables[3]
        self.ships_1 = variables[4]
        self.create_placement_window()

    def create_placement_window(self):
        placement_window = Toplevel(self.gui.window)
        placement_window.resizable(0, 0)
        placement_window.grab_set()
        size = int(self.field_size.split()[0])
        placement_window.geometry(f"{size * 50 + 200}x{size * 50 + 50}")

        letters = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "К", "Л"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]

        field_label = Label(placement_window, text="Игрок 1, расставьте ваши корабли", font=("Roboto", 16))
        field_label.grid(row=0, column=0, columnspan=size + 1, pady=10)

        for k in range(size):
            number_label = Label(placement_window, text=numbers[k])
            number_label.grid(row=k + 2, column=0, padx=10)
            letter_label = Label(placement_window, text=letters[k])
            letter_label.grid(row=1, column=k + 1, pady=10)

        field_buttons = []
        for i in range(size):
            for j in range(size):
                button = Button(placement_window, width=4, height=2)
                button.grid(row=i + 2, column=j + 1)
                field_buttons.append(button)
