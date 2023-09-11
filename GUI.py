from tkinter import *
from tkinter import messagebox
from BotGame import BotGame
from PlayerGame import PlayerGame
import time


class GraphicalInterface:
    def __init__(self):
        self.window = Tk()
        self.window.resizable(0, 0)
        self.window.geometry("500x300")
        self.window.title("Морской бой")
        self.variables = []
        self.play_mode = ""

        frame = Frame(self.window, width=500, height=300)
        frame.pack()
        label = Label(frame, text="Морской бой", font=("Roboto", 20, "bold"))
        label.grid(row=0, column=0, columnspan=2, stick="we", pady=20)
        bot_button = Button(frame, width=50, height=2, text="Игра с ботом", font=("Roboto", 12),
                            command=lambda: self.start_game_with_bot())
        bot_button.grid(row=1, column=0, pady=5)
        player_button = Button(frame, width=50, height=2, text="Игра вдвоем", font=("Roboto", 12),
                               command=lambda: self.start_game_with_player())
        player_button.grid(row=2, column=0, pady=5)

    def run(self):
        self.window.mainloop()

    def start_game_with_bot(self):
        self.play_mode = "bot"
        self.choose_game_options()

    def start_game_with_player(self):
        self.play_mode = "player"
        self.choose_game_options()

    def choose_game_options(self):
        dialog = Toplevel()
        dialog.resizable(0, 0)
        dialog.geometry("400x230")
        dialog.grab_set()

        size_label = Label(dialog, text="Выберите размер поля", font=("Roboto", 12))
        size_label.grid(row=0, column=0, padx=10, pady=5, stick="w")

        size_var = StringVar()
        size_menu = OptionMenu(dialog, size_var, "8 x 8", "9 x 9", "10 x 10", "11 x 11")
        size_var.set("10 x 10")
        size_menu.grid(row=0, column=1)

        ship_4_label = Label(dialog, text="Выберите кол-во кораблей длиной 4", font=("Roboto", 12))
        ship_4_label.grid(row=1, column=0, padx=10, pady=5)

        ship_4_var = IntVar()
        ship_4_menu = OptionMenu(dialog, ship_4_var, 0, 1)
        ship_4_var.set(0)
        ship_4_menu.grid(row=1, column=1)

        ship_3_label = Label(dialog, text="Выберите кол-во кораблей длиной 3", font=("Roboto", 12))
        ship_3_label.grid(row=2, column=0, padx=10, pady=5)

        ship_3_var = IntVar()
        ship_3_menu = OptionMenu(dialog, ship_3_var, 0, 1, 2)
        ship_3_var.set(0)
        ship_3_menu.grid(row=2, column=1)

        ship_2_label = Label(dialog, text="Выберите кол-во кораблей длиной 2", font=("Roboto", 12))
        ship_2_label.grid(row=3, column=0, padx=10, pady=5)

        ship_2_var = IntVar()
        ship_2_menu = OptionMenu(dialog, ship_2_var, 0, 1, 2, 3)
        ship_2_var.set(0)
        ship_2_menu.grid(row=3, column=1)

        ship_1_label = Label(dialog, text="Выберите кол-во кораблей длиной 1", font=("Roboto", 12))
        ship_1_label.grid(row=4, column=0, padx=10, pady=5)

        ship_1_var = IntVar()
        ship_1_menu = OptionMenu(dialog, ship_1_var, 0, 1, 2, 3, 4)
        ship_1_var.set(0)
        ship_1_menu.grid(row=4, column=1)

        ok_button = Button(dialog, text="Готово", width=5, font=("Roboto", 10),
                           command=lambda: self.confirm_variables(size_var, ship_4_var, ship_3_var, ship_2_var,
                                                                  ship_1_var, dialog))
        ok_button.place(x=250, y=190)

        cancel_button = Button(dialog, text="Отмена", width=5, font=("Roboto", 10), command=dialog.destroy)
        cancel_button.place(x=310, y=190)

    def confirm_variables(self, size_var, ship_4_var, ship_3_var, ship_2_var, ship_1_var, dialog):
        self.variables = [size_var.get(), ship_4_var.get(), ship_3_var.get(), ship_2_var.get(), ship_1_var.get()]
        if sum(self.variables[1:]) > 0:
            dialog.destroy()
            self.window.iconify()
            if self.play_mode == "bot":
                bot_game = BotGame(self, self.variables)
            else:
                player_game = PlayerGame(self, self.variables)
        else:
            messagebox.showerror("Ошибка", "Должен быть хотя бы один корабль")
