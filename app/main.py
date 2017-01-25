
class GridManager:
    def __init__(self):
        self.grid = [['.' for x in range(7)] for y in range(6)]

    def show_grid(self):
        return self.grid

    def show_cell_state(self, x, y):
        return self.grid[x][y]

    def change_cell_state(self, Player, x, y):
        self.grid[x][y] = Player.name


class Player:
    def __init__(self, grid_manager, name):
        self.name = name
        self.grid_manager = grid_manager

    def play(self, x):
        try:
            if self.grid_manager.show_cell_state(x, 0) == '.':
                #self.grid_manager.change_cell_state(self, x, 5)
                print self.grid_manager.show_grid()
            else:
                raise ValueError
        except IndexError:
            raise ValueError('Index out of columns')
