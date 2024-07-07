from tkinter import Tk, BOTH, Canvas

class Window:
    # constructor should take a width and height. This will be the size of the new window we create in pixels.       
    def __init__(self, width, height):         
        # should create a new root widget using Tk() and save it as a data member
        self.__root = Tk()

        # Set the title property of the root widget
        self.__root.title("Maze Solver")
        
        # Create a Canvas widget and save it as a data member.
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)

        # Pack the canvas widget so that it's ready to be drawn
        self.__canvas.pack(fill=BOTH, expand=1)

        # Create a data member to represent that the window is "running", and set it to False
        self.__running = False

        # to call the protocol method on the root widget, to connect your close method to the "delete window" action. 
        # This will stop your program from running when you close the graphical window.
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    # method we can call that will redraw all the graphics in the window
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed.")
    
    def close(self):
        self.__running = False
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
