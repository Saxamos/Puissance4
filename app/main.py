
class GridManager:
    def __init__(self):
        self.grid = [['.' for x in range(7)] for y in range(6)]

    def show_grid(self):
        return self.grid

    def show_cell_state(self, x, y):
        return self.grid[y][x]

    def change_cell_state(self, Player, x, y):
        self.grid[y][x] = Player.name


class Player:
    def __init__(self, grid_manager, name):
        self.name = name
        self.grid_manager = grid_manager

    def play(self, x):
        try:
            if self.grid_manager.show_cell_state(x, 0) == '.':
                print self.grid_manager.show_grid()
            else:
                raise ValueError
        except IndexError:
            raise ValueError('Index out of columns')


class GridAnalyser:
    def __init__(self):
        return

    def analyse(self, grid):
        for y in range(6):
            if self.analyse_row(grid, y):
                return 'win'
        for x in range(7):
            if self.analyse_col(grid, x):
                return 'win'
        else:
            return "continue"

    def analyse_row(self, grid, y):
        for x in range(4):
            same_in_a_row = {'x': 0, 'o': 0, '.': 0}
            for j in range(4):
                cell = grid[y][x + j]
                same_in_a_row[cell] += 1
                if (same_in_a_row['x'] == 4) | (same_in_a_row['o'] == 4):
                    return True

    def analyse_col(self, grid, x):
        for y in range(3):
            same_in_a_col = {'x': 0, 'o': 0, '.': 0}
            for j in range(4):
                cell = grid[y + j][x]
                same_in_a_col[cell] += 1
                if (same_in_a_col['x'] == 4) | (same_in_a_col['o'] == 4):
                    return True


class Referee:
    def __init__(self):
        return

    def whose_next(self, grid):
        number_of_x = 0
        for x in range(7):
            for y in range(6):
                if grid[y][x] == 'x':
                    number_of_x += 1
        return 'o' if (number_of_x % 2 == 1) else 'x'

    def start_game(self):
        grid_manager = GridManager()
        return grid_manager.show_grid()

    def display_grid(self, grid_manager):
        return grid_manager.show_grid()
    
    def print_grid(self, grid_manager):
        to_print = ''
        grid = grid_manager.show_grid()
        for row in range(6):
            for column in range(7):
                to_print += grid[row][column]
            to_print += '\t\n'
        print to_print

    def play(self, grid_manager, player, column):
        for row in range(5, -1, -1):
            if grid_manager.show_cell_state(column, row) == '.':
                grid_manager.change_cell_state(player, column, row)
                return True
        return False

def main():
    referee = Referee()
    grid_manager = GridManager()
    grid_analyser = GridAnalyser()
    playerX = Player(grid_manager, 'x')
    playerO = Player(grid_manager, 'o')
    last_player = 'x'
    while grid_analyser.analyse(grid_manager.show_grid()) != '':
        next_player = referee.whose_next(grid_manager.show_grid())
        next_player_instance = playerX if next_player == 'x' else playerO
        print next_player_instance.name

        referee.print_grid(grid_manager)
        print next_player + ' to play !'
        column_to_play = input('Choose a column between 1 to 7 : ')

        while not referee.play(grid_manager, next_player_instance, column_to_play):    
            print 'You can\'t go there, select another column !'
            column_to_play = input('Choose a column between 1 to 7 : ')


if __name__ == '__main__':
    main()
