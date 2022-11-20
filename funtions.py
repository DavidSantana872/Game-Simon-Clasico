from random import randint
import time
import threading
from tkinter import messagebox
wait_time = 0.5
level = 1
try:
    archivo = open("niveles.txt", "r")
    level = archivo.readline()
    archivo.close()
except:
    archivo = open("niveles.txt", "w")
    archivo.write(f"{level}")
    archivo.close()
Array_Colors = []
Array_Colors_Input = []
def consult_level():
    archivo = open("niveles.txt", "r")
    level = archivo.readline()
    archivo.close()
    return level
def Generate_Color():
    i = 0
    level = consult_level()
    for i in range(0, int(level)):
        Array_Colors.append(randint(1, 4))
    i = 0 
def Visual_colors(Array_Colors, button_blue, button_green, button_red, button_yellow, button_start):   
    button_blue.config(state = "disabled")
    button_green.config(state = "disabled")
    button_red.config(state = "disabled")
    button_yellow.config(state = "disabled")
    level = consult_level()
    button_start.config(text = f"NIVEL: {level}", state = "disabled")
    for i in Array_Colors:
        if(i == 2):
            button_blue.config(background="blue")
            time.sleep(wait_time)
            button_blue.config(background="white")
            time.sleep(wait_time)
        elif(i == 3):
            button_green.config(background="green")
            time.sleep(wait_time)
            button_green.config(background="white")
            time.sleep(wait_time)
        elif(i == 1):
            button_red.config(background="red")
            time.sleep(wait_time)
            button_red.config(background="white")
            time.sleep(wait_time)           
        else:
            button_yellow.config(background="yellow")
            time.sleep(wait_time)
            button_yellow.config(background="white")
            time.sleep(wait_time)            
    button_blue.config(state = "normal")
    button_green.config(state = "normal")
    button_red.config(state = "normal")
    button_yellow.config(state = "normal") 
    button_start.config(text = "START GAME!", state = "normal")
    messagebox.showinfo(title="Vamos", message="Tu Turno!")
def start_game(button_blue, button_green, button_red, button_yellow, button_start):
    Array_Colors.clear()
    Array_Colors_Input.clear()
    Generate_Color()
    hilo = threading.Thread(target = Visual_colors, args = (Array_Colors, button_blue, button_green, button_red, button_yellow, button_start))
    hilo.start() 

def get_color(num_color):
    Array_Colors_Input.append(num_color)
    if (len(Array_Colors) != len(Array_Colors_Input)):
        for i in range(0, len(Array_Colors_Input)):
            if(Array_Colors[i] != Array_Colors_Input[i]):
                messagebox.showwarning(title= "Malisimo", message= "Malisimo perdiste")
                Array_Colors.clear()
                Array_Colors_Input.clear()
                num_color = 0
    else:
        if(Array_Colors == Array_Colors_Input):
                level = consult_level()
                messagebox.showinfo(title= "Perfecto", message= f"Vamos al nivel {int(level) + 1}")
                more_level(level)
                Array_Colors.clear()
                Array_Colors_Input.clear()
                num_color = 0
def more_level(level):
    level = consult_level()
    archivo = open("niveles.txt", "w")
    archivo.write(f"{str(int(level)+1)}")
    archivo.close()
