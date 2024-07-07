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
    
    # Calls on the Window class' draw_line function from graphics; win is passed in as a variable
    # so it works in main
    def draw(self, x1, y1, x2, y2):
        if self.has_left_wall is True:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_wall)
        if self.has_right_wall is True:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_wall)
        if self.has_top_wall is True:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_wall)
        if self.has_bottom_wall is True:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_wall)