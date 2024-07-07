from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)
    
    a = Cell(win)
    a.has_right_wall = False
    a.draw(10, 10, 20, 20)

    b = Cell(win)
    b.has_bottom_wall = False
    b.draw(300, 300, 500, 500)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(400, 300, 420, 320)

    d = Cell(win)
    d.has_left_wall = False
    d.draw(750, 550, 790, 590)

    win.wait_for_close()
    

main()