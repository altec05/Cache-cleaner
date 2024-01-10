from tkinter import ttk
from tkinter import *
import tkinter as tk
import variables as vars


def show_about_info(year, root):
    about_win = tk.Toplevel(root)
    about_win.title('О программе')
    about_win.geometry('450x210+300+300')
    about_win.resizable(False, False)
    about_win.minsize(450, 210)
    about_win.maxsize(450, 210)
    appImgB64 = """iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAACXBIWXMAAAsTAAALEwEAmpwYAAACEklEQVR4nO2W30tiQRTH
    /QPrphX0stXDqhu99NI+eCtpjbyuEtqPhyUodp9iXzbKNCsjuTdNHwoiKjEiLArZDMqKXXBv3+UMJTchvFHaSHfgC4eZM9/5cJgzjMlUj6NJDH4RHCFVEEOohRrFkNrQF3bqBqQNE9Es5BxKIiPf4uWrSBBDj7xHV7IQHAuqbsByg2oDyvf+BqDPqOAz7mD+WoXeMa0Uan8H4wd/dQNSbs0Bp+SCbsCLG9XoYhjvoPjKd9DoYu2wO/zQ6q262F7G8QgwuX1Q0lt9FpIaBgPQ9+4qaC9rkkDkCDObF1g9+Vc1wOhxkZ1BZ1VsEm1XU/Lgz118Gouj2RlBpzfGDLomttAzuYvPPzLon8nC9esMrtkc3MFzSME8vOFLJoppjtYoh3J7v2fYXvIgrw7vGvOmM+is8oe6IuBD6WNnd5hP38Izl0Hv1CZso3G0e2Joc62gdXAZLc4lWAYiMPcvQhDDTBTTHK1RTttQFB1fY2wveZAXeZL3U78Z3YC1kmAA5uqggkpQgbKwzing0S1SLa1MFHMHmPCOI221If3RymK+APfzSDU04trjYaJY2fvND2BCCuCwuxt//H4mijekAD+ASbMFV253CfBqeJjNcQOYMltQ0AAWJAkpczM/gImRb9j50M7ASBTTHDeA8mmRAVHVSAzutMgRYO7lMgDlaleQR5nqYfwHZJC3/vq9cOcAAAAASUVORK5CYII="""
    appImgP = tk.PhotoImage(data=appImgB64)
    about_win.iconphoto(False, appImgP)

    f1 = Frame(about_win)
    f1.pack(fill=X, padx=10, pady=3)

    f2 = Frame(about_win)
    f2.pack(fill=X, padx=10, pady=3)

    f3 = Frame(about_win)
    f3.pack(fill=X, padx=10, pady=3)

    f4 = Frame(about_win)
    f4.pack(fill=X, padx=10, pady=3)

    f5 = Frame(about_win)
    f5.pack(fill=X, padx=10, pady=3)

    label1 = ttk.Label(f1, text='Сведения о программе "Очистка кэша"')
    label1.pack(anchor="center", ipadx=1, ipady=2, pady=2)

    label2 = ttk.Label(f2, text=f'© Разработка и права: Домашенко Иван К. / Администратор ИБ ВС')
    label2.pack(anchor="center", ipadx=1, ipady=2, pady=2)

    label3 = ttk.Label(f3, text=f'Программа была разработана в целях очистки временных файлов браузеров'
                                f' Mozilla Firefox и Яндекс Браузера.\n\nВерсия: {vars.version} от {vars.last_update}.',
                       wraplength=400, justify=CENTER, border=1)
    label3.pack(anchor="center", ipadx=1, ipady=2, pady=2)

    label4 = ttk.Label(f4, text=f'КГКУЗ ККЦК №1, г. Красноярск')
    label4.pack(anchor="center", ipadx=1, ipady=2, pady=2)

    label5 = ttk.Label(f5, text=f'2023 - {year}')
    label5.pack(anchor="center", ipadx=1, ipady=2, pady=2)

    about_win.mainloop()
