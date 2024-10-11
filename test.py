import unittest
from maze import Maze
from cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1.cells), num_rows)
        self.assertEqual(len(m1.cells[0]), num_cols)
        self.assertEqual(m1._Maze__num_cols, 12)
        self.assertEqual(m1._Maze__num_rows, 10)

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_rows,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_cols,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        top_left: Cell = m1.cells[0][0]
        bottom_right: Cell = m1.cells[num_rows - 1][num_cols - 1]
        self.assertEqual(top_left.has_top_wall, False)
        self.assertEqual(bottom_right.has_bottom_wall, False)

    def test_reset_visited(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for cell_list in m1.cells:
            for cell in cell_list:
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()