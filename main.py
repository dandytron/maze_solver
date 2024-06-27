from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    l = Line(Point(50,50), Point(200,200))
    win.draw_line(l, "red")
    win.wait_for_close()

main()