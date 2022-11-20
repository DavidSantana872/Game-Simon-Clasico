from funtions import *
from tkinter import *
import threading

class App():
    def __init__(self, windows):
        self.windows = windows
        self.windows.config(bg="#BDBDBD")
        self.button_red = Button(self.windows, text = "RED", height= 10, width= 20, font= "BOLD", background="white", command= lambda: get_color(1))
        self.button_red.grid(row = 0, column = 0)
        self.button_blue = Button(self.windows, text = "BLUE", height= 10, width= 20, font= "BOLD", background="white", command= lambda: get_color(2))
        self.button_blue.grid(row = 1, column = 0)
        self.button_green = Button(self.windows, text = "GREEN", height= 10, width= 20, font= "BOLD", background="white", command= lambda: get_color(3))
        self.button_green.grid(row = 0, column = 1)
        self.button_yellow = Button(self.windows, text = "YELLOW", height= 10, width= 20, font= "BOLD", background="white", command= lambda: get_color(4))
        self.button_yellow.grid(row = 1, column = 1)
        self.button_start = Button(self.windows, text = "START GAME!", background = "black",foreground="white", command= lambda: start_game(self.button_blue, self.button_green, self.button_red, self.button_yellow, self.button_start))
        self.button_start.grid(row= 3, column= 0, columnspan= 2, pady = 10)
if ("__main__" == __name__):
    ventana = Tk()
    ventana.title("Simon Game")
    root = App(ventana)
    ventana.mainloop()
