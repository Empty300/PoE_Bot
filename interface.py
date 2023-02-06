import tkinter as tk

import settings
from bot import main

root = tk.Tk()
root.title("Poe bot")
root.geometry("650x400")

"""Создание фрейма отслеживания хп"""
frame1 = tk.Frame(root, bd=0, relief=tk.GROOVE)
frame1.pack(side="left", fill="both", expand=True, padx=10, pady=10)
tk.Label(frame1, text="Отслеживать хп?").pack()

main_heal = tk.IntVar()
main_heal_checkbox = tk.Checkbutton(frame1, text="Да", variable=main_heal)
main_heal_checkbox.pack(anchor=tk.W)

tk.Label(frame1, text="Используете poe logout macro?\n(Рекомендуется)").pack(pady=10)
options = ["Да (логаут на F1)", "Нет"]
logout_choice = tk.StringVar()
logout_choice.set(settings.logout_macro)
logout_choice_dropdown = tk.OptionMenu(frame1, logout_choice, *options)
logout_choice_dropdown.config(state=tk.DISABLED)
logout_choice_dropdown.pack(anchor=tk.W)

options = ["1", "2", "3", "4", "5"]
heal = tk.StringVar()
tk.Label(frame1, text="Кнопка с банкой на хил:").pack(pady=10)
heal.set(settings.heal_button)
heal_button = tk.OptionMenu(frame1, heal, *options)
heal_button.config(state=tk.DISABLED)
heal_button.pack(anchor=tk.W)


def main_heal_callback(*args):
    if main_heal.get() == 1:
        logout_choice_dropdown.config(state=tk.NORMAL)
        heal_button.config(state=tk.NORMAL)
    else:
        logout_choice_dropdown.config(state=tk.DISABLED)
        heal_button.config(state=tk.DISABLED)


main_heal.trace("w", main_heal_callback)

"""Создание фрейма отслеживания дебаффов"""
frame2 = tk.Frame(root, bd=0, relief=tk.GROOVE)
frame2.pack(side="right", fill="both", expand=True, padx=10, pady=10)
tk.Label(frame2, text="Отслеживать дебафы?").pack()

main_debuff = tk.IntVar()
main_debuff_checkbox = tk.Checkbutton(frame2, text="Да (укажите кнопку с диспелом)", variable=main_debuff)
main_debuff_checkbox.pack(anchor=tk.W)

"""Отслеживание курсы"""

curs = tk.IntVar()
curs.set(settings.track_curs)
curs_checkbox = tk.Checkbutton(frame2, text="Отслеживать и диспелить курсу", variable=curs, state=tk.DISABLED)
curs_checkbox.pack(anchor=tk.W)

button_disp_curs = tk.StringVar()
button_disp_curs.set(settings.curs_button)
disp_curs = tk.OptionMenu(frame2, button_disp_curs, *options)
disp_curs.config(state=tk.DISABLED)
disp_curs.pack(anchor=tk.W)

"""Отслеживание фриза"""

freeze = tk.IntVar()
freeze.set(settings.track_freeze)
freeze_checkbox = tk.Checkbutton(frame2, text="Отслеживать и диспелить фриз", variable=freeze, state=tk.DISABLED)
freeze_checkbox.pack(anchor=tk.W)

button_disp_freeze = tk.StringVar()
button_disp_freeze.set(settings.freeze_button)
disp_freeze = tk.OptionMenu(frame2, button_disp_freeze, *options)
disp_freeze.config(state=tk.DISABLED)
disp_freeze.pack(anchor=tk.W)

"""Отслеживание яда"""

poison = tk.IntVar()
poison.set(settings.track_poison)
poison_checkbox = tk.Checkbutton(frame2, text="Отслеживать и диспелить яд", variable=poison, state=tk.DISABLED)
poison_checkbox.pack(anchor=tk.W)

button_disp_poison = tk.StringVar()
button_disp_poison.set(settings.poison_button)
disp_poison = tk.OptionMenu(frame2, button_disp_poison, *options)
disp_poison.config(state=tk.DISABLED)
disp_poison.pack(anchor=tk.W)

"""Отслеживание блида"""

bleed = tk.IntVar()
bleed.set(settings.track_bleed)
bleed_checkbox = tk.Checkbutton(frame2, text="Отслеживать и диспелить блид", variable=bleed, state=tk.DISABLED)
bleed_checkbox.pack(anchor=tk.W)

button_disp_bleed = tk.StringVar()
button_disp_bleed.set(settings.bleed_button)
disp_bleed = tk.OptionMenu(frame2, button_disp_bleed, *options)
disp_bleed.config(state=tk.DISABLED)
disp_bleed.pack(anchor=tk.W)

"""Отслеживание шока"""

shock = tk.IntVar()
shock.set(settings.track_shock)
shock_checkbox = tk.Checkbutton(frame2, text="Отслеживать и диспелить шок", variable=shock, state=tk.DISABLED)
shock_checkbox.pack(anchor=tk.W)

button_disp_shock = tk.StringVar()
button_disp_shock.set(settings.shock_button)
disp_shock = tk.OptionMenu(frame2, button_disp_shock, *options)
disp_shock.config(state=tk.DISABLED)
disp_shock.pack(anchor=tk.W)


def on_main_debuff_change(*args):
    state = tk.NORMAL if main_debuff.get() else tk.DISABLED
    widgets = [bleed_checkbox, shock_checkbox, freeze_checkbox, poison_checkbox, curs_checkbox,
               disp_bleed, disp_shock, disp_freeze, disp_poison, disp_curs]
    for widget in widgets:
        widget.config(state=state)


main_debuff.trace("w", on_main_debuff_change)


def save_settings():
    with open("settings.py", "w") as file:
        file.write(
            f"track_hp = {main_heal.get()}\n"
            f"logout_macro = '{logout_choice.get()}'\n"
            f"heal_button = '{heal.get()}'\n"
            f"track_debuffs = {main_debuff.get()}\n"
            f"track_curs = {curs.get()}\n"
            f"curs_button = '{button_disp_curs.get()}'\n"
            f"track_freeze = {freeze.get()}\n"
            f"freeze_button = '{button_disp_freeze.get()}'\n"
            f"track_poison = {poison.get()}\n"
            f"poison_button = '{button_disp_poison.get()}'\n"
            f"track_bleed = {bleed.get()}\n"
            f"bleed_button = '{button_disp_bleed.get()}'\n"
            f"track_shock = {shock.get()}\n"
            f"shock_button = '{button_disp_shock.get()}'\n"
        )

    root.destroy()

    main()


frame3 = tk.Frame(root)
frame3.pack(side=tk.BOTTOM, anchor=tk.CENTER, pady=10)

save_button = tk.Button(frame3, text="Сохранить и запустить", command=save_settings)
save_button.grid(row=0, column=0)

root.mainloop()
