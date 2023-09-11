from Ship import Ship


class Field:
    def __init__(self, field_buttons):
        self.field = field_buttons
        self._set_ships()

    def shoot(self, x, y):
        self.field[y][x] = -1
        ship_to_damage = self._try_find_ship_by_cords(x, y)
        if ship_to_damage is not None:
            ship_to_damage.damage()
            if ship_to_damage.length == 0:
                self._cover_dead_ship(ship_to_damage)

    def _set_ships(self):
        for ship in self.ships:
            for cords in ship.coordinates:
                self.field[cords[1]][cords[0]] = 1

    def _try_find_ship_by_cords(self, x, y):
        for ship in self.ships:
            for cords in ship.coordinates:
                if cords[1] == int(y) and cords[0] == int(x):
                    return ship
        return None

    def _cover_dead_ship(self, ship):
        for cords in ship.coordinates:
            self.field[cords[1] + 1][cords[0]] = -1
            self.field[cords[1] - 1][cords[0]] = -1
            self.field[cords[1]][cords[0] + 1] = -1
            self.field[cords[1]][cords[0] - 1] = -1
            self.field[cords[1] + 1][cords[0] + 1] = -1
            self.field[cords[1] + 1][cords[0] - 1] = -1
            self.field[cords[1] - 1][cords[0] - 1] = -1
            self.field[cords[1] - 1][cords[0] + 1] = -1
