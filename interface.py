import tkinter as tk

root = tk.Tk()
root.title("Poe bot")
root.geometry("700x400")

"""Создание фрейма отслеживания хп"""
frame1 = tk.Frame(root, bd=5, relief=tk.GROOVE)
frame1.pack(side="left", fill="both", expand=True)
label = tk.Label(frame1, text="Отслеживать хп?").pack()

main_heal = tk.IntVar()
main_heal_checkbox = tk.Checkbutton(frame1, text="Да", variable=main_heal)
main_heal_checkbox.pack(anchor=tk.W)

label = tk.Label(frame1, text="Используете poe logout macro? (Рекомендуется)").pack()
options = ["Да (логаут на F1)", "Нет"]
logout_choice = tk.StringVar()
logout_choice.set(options[0])
logout_choice_dropdown = tk.OptionMenu(frame1, logout_choice, *options)
logout_choice_dropdown.config(state=tk.DISABLED)
logout_choice_dropdown.pack(anchor=tk.W)

options = ["1", "2", "3", "4", "5"]
heal = tk.StringVar()
heal.set("Кнопка с банкой на хил")
heal = tk.OptionMenu(frame1, heal, *options)
heal.config(state=tk.DISABLED)
heal.pack(anchor=tk.W)


def main_heal_callback(*args):
    if main_heal.get() == 1:
        logout_choice_dropdown.config(state=tk.NORMAL)
        heal.config(state=tk.NORMAL)
    else:
        logout_choice_dropdown.config(state=tk.DISABLED)
        heal.config(state=tk.DISABLED)


main_heal.trace("w", main_heal_callback)

button_disp = tk.StringVar()
button_disp.set("Кнопка с диспелом")

"""Создание фрейма отслеживания дебаффов"""
frame2 = tk.Frame(root, bd=5, relief=tk.GROOVE, width=300, height=300)
frame2.pack(side="right", fill="both", expand=True)
main_label = tk.Label(frame2, text="Отслеживать дебафы?").pack()

main_debuff = tk.IntVar()
main_debuff_checkbox = tk.Checkbutton(frame2, text="Да", variable=main_debuff)
main_debuff_checkbox.pack(anchor=tk.W)

"""Отслеживание курсы"""

curs = tk.IntVar()
curs_checkbox = tk.Checkbutton(frame2, text="Отслеживать и диспелить курсу", variable=curs, state=tk.DISABLED)
curs_checkbox.pack(anchor=tk.W)

disp_curs = tk.OptionMenu(frame2, button_disp, *options)
disp_curs.config(state=tk.DISABLED)
disp_curs.pack(anchor=tk.W)

"""Отслеживание фриза"""

freeze = tk.IntVar()
freeze_checkbox = tk.Checkbutton(frame2, text="Отслеживать и диспелить фриз", variable=freeze, state=tk.DISABLED)
freeze_checkbox.pack(anchor=tk.W)

disp_freeze = tk.OptionMenu(frame2, button_disp, *options)
disp_freeze.config(state=tk.DISABLED)
disp_freeze.pack(anchor=tk.W)

"""Отслеживание яда"""

poison = tk.IntVar()
poison_checkbox = tk.Checkbutton(frame2, text="Отслеживать и диспелить яд", variable=poison, state=tk.DISABLED)
poison_checkbox.pack(anchor=tk.W)

disp_poison = tk.OptionMenu(frame2, button_disp, *options)
disp_poison.config(state=tk.DISABLED)
disp_poison.pack(anchor=tk.W)

"""Отслеживание блида"""

bleed = tk.IntVar()
bleed_checkbox = tk.Checkbutton(frame2, text="Отслеживать и диспелить блид", variable=bleed, state=tk.DISABLED)
bleed_checkbox.pack(anchor=tk.W)

disp_bleed = tk.OptionMenu(frame2, button_disp, *options)
disp_bleed.config(state=tk.DISABLED)
disp_bleed.pack(anchor=tk.W)

"""Отслеживание шока"""

shock = tk.IntVar()
shock_checkbox = tk.Checkbutton(frame2, text="Отслеживать и диспелить шок", variable=shock, state=tk.DISABLED)
shock_checkbox.pack(anchor=tk.W)

disp_shock = tk.OptionMenu(frame2, button_disp, *options)
disp_shock.config(state=tk.DISABLED)
disp_shock.pack(anchor=tk.W)


def on_main_debuff_change(*args):
    state = tk.NORMAL if main_debuff.get() else tk.DISABLED
    widgets = [bleed_checkbox, shock_checkbox, freeze_checkbox, poison_checkbox, curs_checkbox,
               disp_bleed, disp_shock, disp_freeze, disp_poison, disp_curs]
    for widget in widgets:
        widget.config(state=state)


main_debuff.trace("w", on_main_debuff_change)

root.mainloop()
