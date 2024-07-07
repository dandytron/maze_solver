from cell import Cell
from graphics import Window
import time

class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win=None,
                 ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()
    
    # This method should fill a self._cells list with lists of cells. 
    # Each top-level list is a column of Cell objects. Once the matrix is 
    # populated it should call its _draw_cell() method on each Cell.
    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)

        # calling _draw_cell() on each of the cells in the matrix
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)


    # This method should calculate the x/y position of the Cell based on i, j, the cell_size,
    #  and the x/y position of the Maze itself. The x/y position of the maze represents 
    # how many pixels from the top and left the maze should start from the side of the window.

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    # The animate method is what allows us to visualize what the algorithms are doing in real time. 
    # It should simply call the window's redraw() method, then sleep for a short amount of time
    # so your eyes keep up with each render frame. I slept for 0.05 seconds.

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)