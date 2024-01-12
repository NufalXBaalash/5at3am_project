import customtkinter as ctk
from tkinter import *

calculation = 0
foul=0




def next_person():
    text_result.insert("end" , "\n")




def add_to_calculation(symbol,type_name):
    
    global calculation
    calculation += int(symbol)
    text_result.delete(1.0)
    text_result.insert(1.0 , type_name)
    text_result.insert(1.0 , calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0 , "end")
        text_result.insert(1.0 , calculation)
    except:
        clear_field()
        text_result.insert(1.0 , "Error")

def clear_field():
    global calculation
    calculation = 0
    text_result.delete(1.0 , 2.0)


def fplus_food(var):
    global calculation
    calculation = 0
    text_result.insert(1.0 , var)




root = ctk.CTk()
root.geometry("817x636")
root.title("ختعم")
root.resizable(False, False)
root.grid_columnconfigure((8) , weight=2)
root.grid_rowconfigure((4), weight=2)


foul_name = "  فول   "



"""w = ctk.CTkScrollbar(root , height=50 , width=50)
w.grid(row=8 , column=8 , padx=10 , pady=10 ,sticky="ne" , columnspan=10 )
"""


scrollbar = ctk.CTkScrollbar(root , orientation="vertical")
Names = ['Ahmed Baalash', "Yousef Fady" , "Ahmed Foudah"]
"""k = ctk.CTkOptionMenu(root , height= 50, width=120 , font=("Vivaldi", 24) , anchor="w" , values=Names )
k.grid(row=0 , column=8 , padx=20 , pady=20, sticky="e", columnspan=10)
"""
frame2 = ctk.CTkFrame(root , width=340 , height=566 )
frame2.grid_columnconfigure((5) , weight=2)
frame2.grid_rowconfigure((8) , weight=2)
frame2.grid(row=0 , column=0 , padx=20 , pady=20)

text_result = ctk.CTkTextbox(frame2 , height=455 , width= 233, font=("Arial", 20))
text_result.grid(row=0 , column=0 , padx=20 , pady=10, columnspan=10 , sticky="nw")
text_Tperson = ctk.CTkTextbox(frame2 , height=455 , width= 70, font=("Arial", 20))
text_Tperson.grid(row=0 , column=3 , padx=20 , pady=10, columnspan=10 , sticky="ne")
text_total = ctk.CTkTextbox(frame2 , height=68 , width= 290, font=("Arial", 20))
text_total.grid(row=2 , column=0 , padx=20 , pady=10, columnspan=10)



frame= ctk.CTkScrollableFrame(root, height=196 , width=380)
frame.grid_columnconfigure((4) , weight=2)
frame.grid_rowconfigure((8) , weight=2)
Fbtn1 = ctk.CTkButton(frame , text=foul_name , command=lambda: add_to_calculation(1, " فول " ), width=60 , height=40 , font=("Simplified Arabic" , 20))
Fbtn1.grid(row=0 , column=0, padx=5, pady=5)
Fbtn2= ctk.CTkButton(frame, text="طعميه" ,command=lambda: add_to_calculation(1, " طعميه " ), width=60 , height=40, font=("Simplified Arabic" , 20))
Fbtn2.grid(row=0 , column=1, padx=5, pady=5)

frame.grid(row=0 , column=4 , padx=20 , pady=20, sticky="ne", columnspan=10)


frame3 = ctk.CTkFrame(root, height=244 , width=400)
frame3.grid_columnconfigure((4), weight=2)
frame3.grid_rowconfigure((4), weight=2)
frame3.grid(row=0 , column=4 , padx=20, pady=20 , sticky="se" , columnspan=10)

btn_clear = ctk.CTkButton(frame3, text="Clear",command=lambda: clear_field(), height=80 , width=120)
btn_clear.grid(row=0 , column=1 , padx=20 , pady=20)

btn_next = ctk.CTkButton(frame3, height=80 , width=120 , text="Next Person" , command=lambda: next_person())
btn_next.grid(row=0 , column=0 , padx=20 , pady=20 , sticky="w")


combo=ctk.CTkComboBox(root , height=50 , width=250 , values=Names , font=("Arial",20))
combo.grid(row=0 , column=10 , padx=10 , pady=10 , sticky="e")

plus_food = ctk.CTkButton(root,height=60 , width=60 ,text="+" , command=lambda:fplus_food("+"))
plus_food.grid(row=0 , column=4 , padx=20 , pady=20 , sticky="e" , columnspan=2)

























root.mainloop()