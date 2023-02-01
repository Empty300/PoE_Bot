import tkinter as tk

root = tk.Tk()
root.title("Poe bot")
root.geometry("600x300")


"""Создание фрейма отслеживания хп"""
frame1 = tk.Frame(root, bd=5, relief=tk.GROOVE)
frame1.pack(side="left", fill="both", expand=True)
label = tk.Label(frame1, text="Отслеживать хп?").pack()
# Create checkboxes
var1 = tk.IntVar()
checkbox1 = tk.Checkbutton(frame1, text="Да", variable=var1)
checkbox1.pack(anchor=tk.W)

label = tk.Label(frame1, text="Используете poe logout macro? (Рекомендуется)").pack()
options = ["Да (логаут на F1)", "Нет"]
var2 = tk.StringVar()
var2.set(options[0])  # default value
dropdown = tk.OptionMenu(frame1, var2, *options)
dropdown.config(state=tk.DISABLED)
dropdown.pack(anchor=tk.W)

options = ["1", "2", "3", "4", "5"]
var12 = tk.StringVar()
var12.set("Кнопка с банкой на хил")
heal = tk.OptionMenu(frame1, var12, *options)
heal.config(state=tk.DISABLED)
heal.pack(anchor=tk.W)

def checkbox_callback(*args):
    if var1.get() == 1:
        dropdown.config(state=tk.NORMAL)
        heal.config(state=tk.NORMAL)
    else:
        dropdown.config(state=tk.DISABLED)
        heal.config(state=tk.DISABLED)

var1.trace("w", checkbox_callback)


"""Создание фрейма отслеживания дебаффов"""
frame2 = tk.Frame(root, bd=5, relief=tk.GROOVE, width=300, height=300)
frame2.pack(side="right", fill="both", expand=True)
main_label = tk.Label(frame2, text="Отслеживать дебафы?").pack()

var5 = tk.IntVar()
checkbox5 = tk.Checkbutton(frame2, text="Да", variable=var5)
checkbox5.pack(anchor=tk.W)

"""Отслеживание курсы"""


var6 = tk.IntVar()
checkbox6 = tk.Checkbutton(frame2, text="Отслеживать и диспелить курсу", variable=var6)
checkbox6.config(state=tk.DISABLED)
checkbox6.pack(anchor=tk.W)

var9 = tk.StringVar()
var9.set("Кнопка с диспелом")
disp_curs = tk.OptionMenu(frame2, var9, *options)
disp_curs.config(state=tk.DISABLED)
disp_curs.pack(anchor=tk.W)

"""Отслеживание фриза"""

var7 = tk.IntVar()
checkbox7 = tk.Checkbutton(frame2, text="Отслеживать и диспелить фриз", variable=var7, state=tk.DISABLED)
checkbox7.pack(anchor=tk.W)

var10 = tk.StringVar()
var10.set("Кнопка с диспелом")
disp_freeze = tk.OptionMenu(frame2,var10, *options)
disp_freeze.config(state=tk.DISABLED)
disp_freeze.pack(anchor=tk.W)

"""Отслеживание яда"""

var8 = tk.IntVar()
checkbox8 = tk.Checkbutton(frame2, text="Отслеживать и диспелить яд", variable=var8, state=tk.DISABLED)
checkbox8.pack(anchor=tk.W)

var11 = tk.StringVar()
var11.set("Кнопка с диспелом")
disp_poison = tk.OptionMenu(frame2, var11, *options)
disp_poison.config(state=tk.DISABLED)
disp_poison.pack(anchor=tk.W)

def on_var5_change(*args):
    if var5.get() == True:
        checkbox6.config(state=tk.NORMAL)
        checkbox7.config(state=tk.NORMAL)
        checkbox8.config(state=tk.NORMAL)
        disp_curs.config(state=tk.NORMAL)
        disp_freeze.config(state=tk.NORMAL)
        disp_poison.config(state=tk.NORMAL)

    else:
        checkbox6.config(state=tk.DISABLED)
        checkbox7.config(state=tk.DISABLED)
        checkbox8.config(state=tk.DISABLED)
        disp_curs.config(state=tk.DISABLED)
        disp_freeze.config(state=tk.DISABLED)
        disp_poison.config(state=tk.DISABLED)


var5.trace("w", on_var5_change)









root.mainloop()
