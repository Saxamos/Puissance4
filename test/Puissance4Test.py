from __future__ import absolute_import
import unittest
import mock
import patch

from app.main import GridManager, GridAnalyser, Referee, View, Application


class TestGridManager(unittest.TestCase):
    def test_should_return_6_cells_in_x(self):
        # Given
        grid_manager = GridManager()

        # When
        grid = grid_manager.grid

        # Then
        self.assertEqual(len(grid), 6)

    def test_should_return_7_cells_in_y(self):
        # Given
        grid_manager = GridManager()

        # When
        grid = grid_manager.grid

        # Then
        self.assertEqual(len(grid[0]), 7)

    def test_should_print_7x6_empty_cells(self):
        # Given
        grid_manager = GridManager()
        result_grid =  [['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.']]

        # When
        grid = grid_manager.show_grid()

        # Then
        self.assertEqual(result_grid, grid)

    def test_should_return_cell_state_0x0(self):
        # Given
        grid_manager = GridManager()
        cell_not_played = '.'

        # When
        cell_state = grid_manager.show_cell_state(0, 0)

        # Then
        self.assertEqual(cell_state, cell_not_played)

    def test_should_return_cell_state_4x2(self):
        # Given
        grid_manager = GridManager()
        cell_played = 'o'
        player = 'o'

        # When
        grid_manager.change_cell_state(player, 4, 2)
        cell_state = grid_manager.show_cell_state(4, 2)

        # Then
        self.assertEqual(cell_state, cell_played)


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
        grid_manager = GridManager()
        player1 = 'x'
        player2 = 'o'
        result_grid = [['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['x', 'o', '.', '.', '.', '.', '.']]
        # When
        grid_manager.change_cell_state(player1, 0, 5)
        grid_manager.change_cell_state(player2, 1, 5)

        # Then
        self.assertEqual(result_grid, referee.display_grid(grid_manager))

    def test_should_add_a_first_coin_and_return_the_grid(self):
        # Given
        referee = Referee()
        grid_manager = GridManager()
        player1 = 'x'
        result_grid = [['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['x', '.', '.', '.', '.', '.', '.']]
        # When
        referee.play(grid_manager, player1, 0)
        new_grid = grid_manager.show_grid()
        # Then
        self.assertEqual(result_grid, new_grid)

    def test_should_add_a_second_coin_and_return_the_grid(self):
        # Given
        referee = Referee()
        grid_manager = GridManager()
        player1 = 'x'
        player2 = 'o'
        result_grid = [['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['o', '.', '.', '.', '.', '.', '.'],
                       ['x', '.', '.', '.', '.', '.', '.']]
        # When
        grid_manager.change_cell_state(player1, 0, 5)
        referee.play(grid_manager, player2, 0)
        new_grid = grid_manager.show_grid()

        # Then
        self.assertEqual(result_grid, new_grid)

    def test_should_add_a_third_coin_and_return_the_grid(self):
        # Given
        referee = Referee()
        grid_manager = GridManager()
        player1 = 'x'
        player2 = 'o'
        result_grid = [['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.'],
                       ['x', '.', '.', '.', '.', '.', '.'],
                       ['o', '.', '.', '.', '.', '.', '.'],
                       ['x', '.', '.', '.', '.', '.', '.']]
        # When
        grid_manager.change_cell_state(player1, 0, 5)
        grid_manager.change_cell_state(player2, 0, 4)
        referee.play(grid_manager, player1, 0)
        new_grid = grid_manager.show_grid()

        # Then
        self.assertEqual(result_grid, new_grid)

    def test_should_add_a_third_coin_and_return_true_when_column_is_not_full(self):
        # Given
        referee = Referee()
        grid_manager = GridManager()
        player1 = 'x'
        player2 = 'o'
        
        # When
        grid_manager.change_cell_state(player1, 0, 5)
        grid_manager.change_cell_state(player2, 0, 4)
        returned_boolean = referee.play(grid_manager, player1, 0)

        # Then
        self.assertEqual(True, returned_boolean)

    def test_should_add_a_third_coin_and_return_false_when_column_is_full(self):
        # Given
        referee = Referee()
        grid_manager = GridManager()
        player1 = 'x'
        player2 = 'o'
        
        # When
        grid_manager.change_cell_state(player1, 0, 5)
        grid_manager.change_cell_state(player2, 0, 4)
        grid_manager.change_cell_state(player2, 0, 3)
        grid_manager.change_cell_state(player2, 0, 2)
        grid_manager.change_cell_state(player2, 0, 1)
        grid_manager.change_cell_state(player2, 0, 0)
        returned_boolean = referee.play(grid_manager, player1, 0)

        # Then
        self.assertEqual(False, returned_boolean)

    def test_should_say_continue(self):
        # Given
        referee = Referee()
        analyser = GridAnalyser()
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
        analyser = GridAnalyser()
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
        analyser = GridAnalyser()
        grid = [['.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.'],
                ['.', 'o', '.', '.', '.', '.', '.'],
                ['.', 'o', '.', '.', '.', '.', '.'],
                ['x', 'o', 'x', '.', '.', '.', '.'],
                ['x', 'o', 'x', '.', '.', '.', '.']]
        # When

        # Then
        self.assertEqual(referee.game_status(grid), 'o win')


class TestApplication(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
