from __future__ import absolute_import
import unittest

from app.main import GridManager, Player


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
        player = Player(grid_manager, 'o')

        # When
        grid_manager.change_cell_state(player, 4, 2)
        cell_state = grid_manager.show_cell_state(4, 2)

        # Then
        self.assertEqual(cell_state, cell_played)

    def test_should_return_0x5_coordinates_after_played_in_col_0_and_empty_grid(self):
        # Given
        grid_manager = GridManager()
        player = Player(grid_manager, 'o')
        result_cell_location = (0, 5)

        # When
        cell_location = player.play(0)

        # Then
        self.assertEqual(cell_location, result_cell_location)


class TestPlayer(unittest.TestCase):
    def test_should_raise_error_if_play_outside_column_grid(self):
        # Given
        grid_manager = GridManager()
        player = Player(grid_manager, 'x')

        # When
        choice = 7

        # Then
        self.assertRaises(ValueError, player.play, choice)

    def test_should_raise_error_if_play_in_full_column(self):
        # Given
        grid_manager = GridManager()
        player = Player(grid_manager, 'x')

        # When
        grid_manager.change_cell_state(player, 0, 0)

        # Then
        self.assertRaises(ValueError, player.play, 0)


if __name__ == '__main__':
    unittest.main()