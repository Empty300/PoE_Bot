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

def checkbox_callback(*args):
    if var1.get() == 1:
        dropdown.config(state=tk.NORMAL)
    else:
        dropdown.config(state=tk.DISABLED)

var1.trace("w", checkbox_callback)


"""Создание фрейма отслеживания дебаффов"""
frame2 = tk.Frame(root, bd=5, relief=tk.GROOVE, width=300, height=300)
frame2.pack(side="right", fill="both", expand=True)
label = tk.Label(frame2, text="Отслеживать дебафы?").pack()

var5 = tk.IntVar()
checkbox5 = tk.Checkbutton(frame2, text="Да", variable=var5)
checkbox5.pack(anchor=tk.W)

var6 = tk.IntVar()
checkbox6 = tk.Checkbutton(frame2, text="Option 6", variable=var6, state=tk.DISABLED)
checkbox6.pack(anchor=tk.W)
options = ["Option 1", "Option 2", "Option 3"]
var3 = tk.StringVar()
var3.set(options[0])  # default value
option_menu = tk.OptionMenu(frame2, var3, *options)
option_menu.pack(anchor=tk.W)

var7 = tk.IntVar()
checkbox7 = tk.Checkbutton(frame2, text="Option 7", variable=var7, state=tk.DISABLED)
checkbox7.pack(anchor=tk.W)
options = ["Option 1", "Option 2", "Option 3"]
var4 = tk.StringVar()
var4.set(options[0])  # default value
options = ["Option 1", "Option 2", "Option 3"]
option_menu = tk.OptionMenu(frame2,var4, *options)
option_menu.pack(anchor=tk.W)

var8 = tk.IntVar()
checkbox8 = tk.Checkbutton(frame2, text="Option 8", variable=var8, state=tk.DISABLED)
checkbox8.pack(anchor=tk.W)
options = ["Option 1", "Option 2", "Option 3"]
var5 = tk.StringVar()
var5.set(options[0])  # default value
option_menu = tk.OptionMenu(frame2,var5, *options)
option_menu.pack(anchor=tk.W)

def on_var5_change(*args):
    if var5.get() == 1:
        checkbox6.config(state=tk.NORMAL)
        checkbox7.config(state=tk.NORMAL)
        checkbox8.config(state=tk.NORMAL)
    else:
        checkbox6.config(state=tk.DISABLED)
        checkbox7.config(state=tk.DISABLED)
        checkbox8.config(state=tk.DISABLED)

var5.trace("w", on_var5_change)
var6 = tk.StringVar(frame2)
var6.set("Option 1") # default value







root.mainloop()
