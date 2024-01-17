import customtkinter as ctk
from tkinter import *
import tkinter as tk
from openpyxl import load_workbook

wb = load_workbook("E:\College\C++ Codes\Python Codes\Khat3am_Project\Khat3am.xlsx", data_only=True)
ws = wb.active



calculation = 0
foul=0






def next_person():
    text_result.insert("end" , "\n")

def open_new_window():
    new_window = Toplevel(root)
    new_window.title("Final Order")
    new_window.geometry("500x420")
    new_window.grid_columnconfigure((4) , weight=2)
    new_window.grid_rowconfigure((4) , weight=2)
    Final_order = tk.Text(new_window , height=4 , width=35 , font=("Arial", 18))
    Final_order.grid(row=1 , column=0 , sticky="n" , padx=20 , pady=10 , columnspan=5)
    for row in range(2, 48):  # Adjust the range to match your requirements
        column_J = ws['J' + str(row)].value                                                #Name Column
        value_A = ws['A' + str(row)].value                                                 #Name Row

        if column_J is not None and value_A is not None and value_A != 0:
            Final_order.insert( 1.0  , f" Name : {column_J} , Pay : {value_A}\n")
    All_types = tk.Text(new_window, height=3 , width=40 , font=("Arial" , 20))
    All_types.grid(row=0 , column=0 , padx=20 , pady=10 , columnspan=5)
    Total = tk.Text(new_window, height=3 , width=40 , font=("Arial" , 20))
    Total.grid(row=2 , column=0 , padx=20 , pady=10 , columnspan=5)
    total_cost = ws['E51'].value                                           # Total Place
    Total.insert(1.0 , f"Total : {total_cost}")
    for column in range(66 , 73):
        row_51 = "49"
        all_totals = ws[chr(column) + row_51].value
        type_per_num = ws[chr(column) + "1"].value

        if all_totals is not None and all_totals !=0:
            All_types.insert(1.0 , f"{type_per_num} : {all_totals}\n")
names = []
for i in range (2 , 48):
    x = ws['J' + str(i)].value
    names.append(x)


def clear_field():
    global calculation
    calculation = 0
    text_result.delete(1.0 , 2.0)


def fplus_food(var):
    global calculation
    calculation = 0
    text_result.insert(1.0 , var)


def search_items():
    search_value = variable.get().lower()
    if not search_value.strip():
        combo_names['values'] = item_names
    else:
        value_to_display = [str(value) for value in item_names if search_value in str(value).lower()]
        combo_names['values'] = value_to_display


root = ctk.CTk()
root.geometry("817x636")
root.title("ختعم")
#root.resizable(False, False)
root.grid_columnconfigure((8) , weight=2)
root.grid_rowconfigure((4), weight=2)





foul_name = "  فول   "



scrollbar = ctk.CTkScrollbar(root , orientation="vertical")
Names = ['Ahmed Baalash', "Yousef Fady" , "Ahmed Foudah"]
"""k = ctk.CTkOptionMenu(root , height= 50, width=120 , font=("Vivaldi", 24) , anchor="w" , values=Names )
k.grid(row=0 , column=8 , padx=20 , pady=20, sticky="e", columnspan=10)
"""
frame2 = ctk.CTkFrame(root , width=340 , height=566 )
frame2.grid_columnconfigure((5) , weight=2)
frame2.grid_rowconfigure((8) , weight=2)
frame2.grid(row=0 , column=0 , padx=20 , pady=20)

text_result = ctk.CTkTextbox(frame2 , height=455 , width= 150, font=("Arial", 20))
text_result.grid(row=2 , column=0 , padx=20 , pady=10, columnspan=10 , sticky="nw")
text_Tperson = ctk.CTkTextbox(frame2 , height=455 , width= 150, font=("Arial", 20))
text_Tperson.grid(row=2 , column=3 , padx=20 , pady=10, columnspan=10 , sticky="ne")
text_total = ctk.CTkTextbox(frame2 , height=68 , width= 290, font=("Arial", 20))
text_total.grid(row=0 , column=0 , padx=20 , pady=10, columnspan=10)



frame= ctk.CTkScrollableFrame(root, height=196 , width=380)
frame.grid_columnconfigure((4) , weight=2)
frame.grid_rowconfigure((8) , weight=2)
Fbtn1 = ctk.CTkButton(frame , text=foul_name , command=lambda: add_to_calculation(1, " فول " ), width=60 , height=40 , font=("Simplified Arabic" , 20))
Fbtn1.grid(row=0 , column=0, padx=5, pady=5)
Fbtn2= ctk.CTkButton(frame, text="طعميه" ,command=lambda: add_to_calculation(1, " طعميه " ), width=60 , height=40, font=("Simplified Arabic" , 20))
Fbtn2.grid(row=0 , column=1, padx=5, pady=5)

frame.grid(row=0 , column=4 , padx=20 , pady=20, sticky="ne", columnspan=10)


frame3 = ctk.CTkFrame(root, height=244 , width=460)
frame3.grid_columnconfigure((4), weight=2)
frame3.grid_rowconfigure((4), weight=2)
frame3.grid(row=0 , column=4 , padx=20, pady=20 , sticky="se" , columnspan=10)

btn_clear = ctk.CTkButton(frame3, text="Clear",command=lambda: clear_field(), height=80 , width=80)
btn_clear.grid(row=0 , column=1 , padx=20 , pady=20)

btn_next = ctk.CTkButton(frame3, height=80 , width=80 , text="Next Person" , command=lambda: next_person())
btn_next.grid(row=0 , column=0 , padx=20 , pady=20 , sticky="w")

btn_order = ctk.CTkButton(frame3, height=80, width=80 , command=lambda: open_new_window(), text="Order"  )
btn_order.grid(row=0 , column=2 , padx=20 , pady=20)

"""combo=ctk.CTkComboBox(root , height=50 , width=250 , values=Names , font=("Arial",20))
combo.grid(row=0 , column=10 , padx=10 , pady=10 , sticky="e")
"""
"""plus_food = ctk.CTkButton(root,height=60 , width=60 ,text="+" , command=lambda:fplus_food("+"))
plus_food.grid(row=0 , column=4 , padx=20 , pady=20 , sticky="e" , columnspan=2)
"""
frame4 = ctk.CTkFrame(root , width=402 , height=120 )
frame4.grid_columnconfigure((4) , weight=2)
frame4.grid_rowconfigure((4) , weight=2)

frame4.grid(row=0 , column=8 , padx=20 , pady=20 , sticky="e")

add_btn = ctk.CTkButton(frame4 , height=50 , width=50 , text=" + " ,font=("Arial" , 26) , corner_radius=90)
add_btn.grid(row=2 , column=1 , padx=10 , pady=20 , columnspan=1)

minus_btn = ctk.CTkButton(frame4 , height=50 , width=50 , text=" - "  , font=("Arial" , 28) , corner_radius=90)
minus_btn.grid(row=2 , column=0 , padx=20 , pady=20 , columnspan=1)

combo_names = ctk.CTkComboBox(frame4 , height=20 , width=300 , font=("Arial" , 16) , values=names , )
combo_names.grid(row=0 , column=0 , padx=20 , pady=0 , sticky="e" , columnspan=5)


item_names = names
variable = StringVar()
combo_names['values'] = item_names

variable = StringVar()
entry1 = ctk.CTkEntry(frame4, textvariable=variable , height=20 , width=250)
entry1.grid(row=1 , column=0 , padx=20 , pady=0 , columnspan=5 , sticky="e")

Search_btn = ctk.CTkButton(frame4, text="Search", command=lambda:search_items , height=50 , width=100 , corner_radius=20)
Search_btn.grid(row=2 , column = 3 , padx=20 , pady=5)




















root.mainloop()
