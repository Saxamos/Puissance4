
class GridManager:
    def __init__(self):
        self.grid = [['.' for x in range(7)] for y in range(6)]

    def show_grid(self):
        return self.grid

    def show_cell_state(self, x, y):
        return self.grid[y][x]

    def change_cell_state(self, player, x, y):
        self.grid[y][x] = player


class Grid:
    def __init__(self):
        self.grid = [['.' for x in range(7)] for y in range(6)]


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
        if self.analyse_high_diag(grid):
            return 'win'
        for x in range(7):
            for y in range(6):
                if grid[y][x] == '.':
                    return 'continue'
        return 'draw'

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

    def analyse_high_diag(self, grid):
        for i in range(3):
            for j in range(4):
                if (grid[5-i][0+j] == 'x') & (grid[4-i][1+j] == 'x') & (grid[3-i][2+j] == 'x') & (grid[2-i][3+j] == 'x'):
                    return True
                if (grid[5-i][0+j] == 'o') & (grid[4-i][1+j] == 'o') & (grid[3-i][2+j] == 'o') & (grid[2-i][3+j] == 'o'):
                    return True


class Referee:
    def __init__(self):
        return

    def whose_next(self, grid):
        number_of_coins = 0
        for x in range(7):
            for y in range(6):
                if grid[y][x] != '.':
                    number_of_coins += 1
        return 'o' if (number_of_coins % 2 == 1) else 'x'

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
        if column > len(grid_manager.show_grid()[0]) or column < 0:
            return False
        for row in range(5, -1, -1):
            if grid_manager.show_cell_state(column, row) == '.':
                grid_manager.change_cell_state(player, column, row)
                return True
        return False

    def game_status(self, grid):
        analyser = GridAnalyser()
        whose_next = self.whose_next(grid)
        result = analyser.analyse(grid)
        if result == 'win':
            return 'o win' if whose_next == 'x' else 'x win'
        else:
            return result


class Application:
    def __init__(self, view, referee, grid_manager):
        self.view = view
        self.referee = referee
        self.grid_manager = grid_manager
        return

    def play(self):
        while self.referee.game_status(self.grid_manager.show_grid()) == 'continue':
            next_player = self.referee.whose_next(self.grid_manager.show_grid())

            self.referee.print_grid(self.grid_manager)
            self.view.display(next_player + ' turn !')
            column_to_play = input('Choose a column between 1 and 7 : ') - 1

            while not self.referee.play(self.grid_manager, next_player, column_to_play):
                self.view.display('You can\'t go there, select another column !')
                column_to_play = input('Choose a column between 1 to 7 : ') - 1

        self.view.display(self.referee.print_grid(self.grid_manager))
        self.view.display(self.referee.game_status(self.grid_manager.show_grid()))


class View:
    def __init__(self):
        return

    def display(self, string):
        print string



if __name__ == '__main__':
    app = Application()
    app.play()
