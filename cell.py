from graphics import Line, Point

# Class that holds all the data about an individual cell. 
# It should know which walls it has, where it exists on the canvas in x/y coordinates,
# and access to the window so that it can draw itself

class Cell:
    def __init__(self, win) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        # x1, y1 are the top-left corner coordinates. x2, y2 are the bottom-right corner coordinates
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

        # this data member tracks whether the cell is visited, a form of depth-first traversal
        self.visited = False
    
    # Calls on the Window class' draw_line function from graphics; win is passed in as a variable
    # so it works in main
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2   

        left_wall = Line(Point(x1, y1), Point(x1, y2))
        right_wall = Line(Point(x2, y1), Point(x2, y2))
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        bottom_wall = Line(Point(x1, y2), Point(x2, y2))

        if self.has_left_wall:
            self._win.draw_line(left_wall)
        else:
            self._win.draw_line(left_wall, "white")

        if self.has_right_wall:
            self._win.draw_line(right_wall)
        else:
            self._win.draw_line(right_wall, "white")

        if self.has_top_wall:
            self._win.draw_line(top_wall)
        else:
            self._win.draw_line(top_wall, "white")

        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall)
        else:
            self._win.draw_line(bottom_wall, "white")

    # Next, we need a way to draw a path between 2 cells. It should draw a line from the center of one cell to another
    # Using integer division here, we don't need it to be super exact
    def draw_move(self, to_cell, undo=False):

        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        line_color = "red"
        if undo:
            line_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, line_color)