import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_create_cells_larger(self):
        num_cols = 18
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_wall_break(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows,num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False
        )

    def test_reset_visited_cells(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows,num_cols, 10, 10)
        for column in m1._cells:
            for cell in column:
                self.assertEqual(
                    cell.visited,
                    False
                )
                

if __name__ == "__main__":
    unittest.main()