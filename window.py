from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height) -> None:
        # constructor should take a width and height. This will be the size of the new window we create in pixels.
        self.width = width
        self.height = height
        
        # should create a new root widget using Tk() and save it as a data member
        self.root = Tk()
        # Set the title property of the root widget
        self.root.title("TBD Title")
        
        # Create a Canvas widget and save it as a data member.
        self.canvas = Canvas()
        # Pack the canvas widget so that it's ready to be drawn
        self.canvas.pack()

        # Create a data member to represent that the window is "running", and set it to False
        self.window_is_running = False
    
    # method we can call that will redraw all the graphics in the window
    def redraw():
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close():
        self.window_is_running = True
    
    def close():