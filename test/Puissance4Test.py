from __future__ import absolute_import
import unittest

from app.main import Grid, GridAnalyser, Referee, View, Application


class TestGrid(unittest.TestCase):
    def test_should_return_6_cells_in_x(self):
        # Given
        grid = Grid()

        # When

        # Then
        self.assertEqual(len(grid.grid), 6)

    def test_should_return_7_cells_in_y(self):
        # Given
        grid = Grid()

        # When

        # Then
        self.assertEqual(len(grid.grid[0]), 7)

    def test_should_print_7x6_empty_cells(self):
        # Given
        grid = Grid()
        result_grid  = [['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.']]

        # When

        # Then
        self.assertEqual(result_grid, grid.grid)

    def test_should_return_cell_state_0x0(self):
        # Given
        grid = Grid()
        cell_not_played = '.'

        # When
        cell_state = grid.grid[0][0]

        # Then
        self.assertEqual(cell_state, cell_not_played)

    def test_should_return_cell_state(self):
        # Given
        grid = Grid()
        result_grid =  [['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['o', '.', '.', '.', '.', '.', '.']]
        player = 'o'

        # When
        grid.grid[5][0] = player

        # Then
        self.assertEqual(result_grid[5][0], grid.grid[5][0])


class TestGridAnalyser(unittest.TestCase):
    def test_should_continue_if_grid_not_full_and_nobody_win(self):
        # Given
        grid_analyser = GridAnalyser()

        # When
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', 'o', '.', '.', '.', '.', '.']]

        # Then
        self.assertEqual(grid_analyser.analyse(grid), "continue")

    def test_should_stop_and_say_win_case_1(self):
        # Given
        grid_analyser = GridAnalyser()

        # When
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['o', '.', '.', '.', '.', '.', '.'],
                ['o', '.', '.', '.', '.', '.', '.'],
                ['o', '.', '.', '.', '.', '.', '.'],
                ['x', 'x', 'x', 'x', '.', '.', '.']]
        # Then
        self.assertEqual("win", grid_analyser.analyse(grid))
        
    def test_should_stop_and_say_win_case_2(self):
        # Given
        grid_analyser = GridAnalyser()

        # When
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['x', '.', '.', '.', '.', '.', '.'],
                ['x', '.', '.', '.', '.', '.', '.'],
                ['x', '.', '.', '.', '.', '.', '.'],
                ['o', 'o', 'o', 'o', '.', '.', '.']]
        # Then
        self.assertEqual("win", grid_analyser.analyse(grid))

    def test_should_stop_and_say_win_case_3(self):
        # Given
        grid_analyser = GridAnalyser()

        # When
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['x', '.', 'o', '.', '.', '.', '.'],
                ['x', 'o', 'o', '.', '.', '.', '.'],
                ['x', 'x', 'x', 'x', '.', '.', '.'],
                ['o', 'x', 'o', 'o', '.', '.', '.']]
        # Then
        self.assertEqual("win", grid_analyser.analyse(grid))

    def test_should_stop_and_say_win_case_4(self):
        # Given
        grid_analyser = GridAnalyser()

        # When
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['x', '.', 'o', '.', '.', '.', '.'],
                ['x', 'o', 'o', '.', '.', '.', '.'],
                ['x', 'x', 'o', 'x', '.', '.', '.'],
                ['o', 'x', 'o', 'o', '.', '.', '.']]
        # Then
        self.assertEqual("win", grid_analyser.analyse(grid))

    def test_should_return_draw(self):
        # Given
        grid_analyser = GridAnalyser()

        # When
        grid = [['o', 'o', 'x', 'o', 'o', 'o', 'x'],
                ['x', 'x', 'o', 'x', 'x', 'x', 'o'],
                ['o', 'o', 'o', 'x', 'o', 'o', 'x'],
                ['x', 'o', 'x', 'o', 'x', 'x', 'x'],
                ['o', 'o', 'o', 'x', 'o', 'x', 'o'],
                ['x', 'x', 'o', 'o', 'x', 'o', 'x']]
        # Then
        self.assertEqual("draw", grid_analyser.analyse(grid))

    def test_should_return_win_with_high_diagonal1(self):
        # Given
        grid_analyser = GridAnalyser()

        # When
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', 'x', '.', '.', '.'],
                ['.', '.', 'x', 'x', '.', '.', '.'],
                ['.', 'x', 'o', 'o', '.', '.', '.'],
                ['x', 'x', 'o', 'o', 'o', '.', '.']]
        # Then
        self.assertEqual("win", grid_analyser.analyse(grid))

    def test_should_return_win_with_high_diagonal2(self):
        # Given
        grid_analyser = GridAnalyser()

        # When
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', 'x', 'x', '.', '.'],
                ['.', '.', 'x', 'o', 'x', '.', '.'],
                ['.', 'x', 'x', 'o', 'o', '.', '.'],
                ['x', 'x', 'o', 'o', 'x', '.', '.'],
                ['o', 'x', 'o', 'o', 'o', '.', '.']]
        # Then
        self.assertEqual("win", grid_analyser.analyse(grid))

    def test_should_return_win_with_high_diagonal3(self):
        # Given
        grid_analyser = GridAnalyser()

        # When
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', 'o', '.', '.', '.'],
                ['.', '.', 'o', 'x', '.', '.', '.'],
                ['.', 'o', 'x', 'o', '.', '.', '.'],
                ['o', 'x', 'x', 'x', '.', '.', '.']]
        # Then
        self.assertEqual("win", grid_analyser.analyse(grid))

    def test_should_return_win_with_high_diagonal4(self):
        # Given
        grid_analyser = GridAnalyser()

        # When
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', 'o', '.', '.'],
                ['.', '.', 'x', 'o', 'o', '.', '.'],
                ['x', 'x', 'o', 'o', 'x', '.', '.'],
                ['o', 'o', 'x', 'x', 'x', '.', '.']]
        # Then
        self.assertEqual("win", grid_analyser.analyse(grid))


class TestReferee(unittest.TestCase):
    def test_should_select_player_x_with_empty_grid(self):
        # Given
        referee = Referee()

        # When
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.']]
        # Then
        self.assertEqual("x", referee.whose_next(grid))

    def test_should_select_player_o_when_x_played_at_0x5(self):
        # Given
        referee = Referee()

        # When
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['x', '.', '.', '.', '.', '.', '.']]
        # Then
        self.assertEqual("o", referee.whose_next(grid))

    def test_should_select_player_o_when_x_played_at_1x5(self):
        # Given
        referee = Referee()

        # When
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', 'x', '.', '.', '.', '.', '.']]
        # Then
        self.assertEqual("o", referee.whose_next(grid))

    def test_should_select_player_x_when_o_played_two_times(self):
        # Given
        referee = Referee()

        # When
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['o', 'x', 'o', 'x', '.', '.', '.']]
        # Then
        self.assertEqual("x", referee.whose_next(grid))

    def test_should_start_game(self):
        # Given
        referee = Referee()

        # When
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.']]
        # Then
        self.assertEqual(grid, referee.start_game())

    def test_should_display_grid(self):
        # Given
        referee = Referee()
        grid = Grid().grid
        player1 = 'x'
        player2 = 'o'
        result_grid = [['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['x', 'o', '.', '.', '.', '.', '.']]
        # When
        grid[5][0] =  player1
        grid[5][1] =  player2

        # Then
        self.assertEqual(result_grid, referee.display_grid(grid))

    def test_should_add_a_first_coin_and_return_the_grid(self):
        # Given
        referee = Referee()
        grid = Grid()

        player1 = 'x'
        result_grid = [['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['x', '.', '.', '.', '.', '.', '.']]
        # When
        referee.play(grid.grid, player1, 0)
        new_grid = grid.grid
        # Then
        self.assertEqual(result_grid, new_grid)

    def test_should_add_a_second_coin_and_return_the_grid(self):
        # Given
        referee = Referee()
        grid = Grid().grid
        player1 = 'x'
        player2 = 'o'
        result_grid = [['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['o', '.', '.', '.', '.', '.', '.'],
                       ['x', '.', '.', '.', '.', '.', '.']]
        # When
        grid[5][0] = player1
        referee.play(grid, player2, 0)

        # Then
        self.assertEqual(result_grid, grid)

    def test_should_add_a_third_coin_and_return_the_grid(self):
        # Given
        referee = Referee()
        grid = Grid().grid
        player1 = 'x'
        player2 = 'o'
        result_grid = [['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['x', '.', '.', '.', '.', '.', '.'],
                       ['o', '.', '.', '.', '.', '.', '.'],
                       ['x', '.', '.', '.', '.', '.', '.']]
        # When
        grid[5][0] =  player1
        grid[4][0] =  player2
        referee.play(grid, player1, 0)

        # Then
        self.assertEqual(result_grid, grid)

    def test_should_add_a_third_coin_and_return_true_when_column_is_not_full(self):
        # Given
        referee = Referee()
        grid = Grid().grid
        player1 = 'x'
        player2 = 'o'
        
        # When
        grid[5][0] = player1
        grid[4][0] = player2
        returned_boolean = referee.play(grid, player1, 0)

        # Then
        self.assertEqual(True, returned_boolean)

    def test_should_add_a_third_coin_and_return_false_when_column_is_full(self):
        # Given
        referee = Referee()
        player1 = 'x'
        result_grid = [['o', '.', '.', '.', '.', '.', '.'],
                       ['x', '.', '.', '.', '.', '.', '.'],
                       ['o', '.', '.', '.', '.', '.', '.'],
                       ['x', '.', '.', '.', '.', '.', '.'],
                       ['o', '.', '.', '.', '.', '.', '.'],
                       ['x', '.', '.', '.', '.', '.', '.']]
        
        # When
        returned_boolean = referee.play(result_grid, player1, 0)

        # Then
        self.assertEqual(False, returned_boolean)

    def test_should_say_continue(self):
        # Given
        referee = Referee()
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['x', '.', '.', '.', '.', '.', '.']]
        # When

        # Then
        self.assertEqual(referee.game_status(grid), 'continue')

    def test_should_say_x_win(self):
        # Given
        referee = Referee()
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['o', '.', '.', '.', '.', '.', '.'],
                ['o', 'o', '.', '.', '.', '.', '.'],
                ['x', 'x', 'x', 'x', '.', '.', '.']]
        # When

        # Then
        self.assertEqual(referee.game_status(grid), 'x win')

    def test_should_say_o_win(self):
        # Given
        referee = Referee()
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', 'o', '.', '.', '.', '.', '.'],
                ['.', 'o', '.', '.', '.', '.', '.'],
                ['x', 'o', 'x', '.', '.', '.', '.'],
                ['x', 'o', 'x', '.', '.', '.', '.']]
        # When

        # Then
        self.assertEqual(referee.game_status(grid), 'o win')


'''class TestApplication(unittest.TestCase):

    @mock.patch('app.main.View')
    @mock.patch('app.main.GridManager')
    @mock.patch('app.main.Referee')
    def test_print(self, mock_referee, mock_grid_manager,  mock_view):
        # Given
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.']]

        mock_view.input.return_value = 3
        mock_grid_manager.show_grid.side_effects = [grid, grid]
        mock_referee.print_grid.return_value = grid
        mock_referee.game_status(grid).return_value = 'win'
        mock_referee.whose_next(grid).return_value = 'x'

        app = Application(mock_view, mock_referee, mock_grid_manager)

        # When
        app.play()


        # Then
        mock_view.display.assert_called_with(grid)
'''

if __name__ == '__main__':
    unittest.main()
