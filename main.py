from tkinter import *
import tkinter as tk
import datetime
from tkinter import ttk
import ttkthemes as TTk
from datetime import datetime
import threading


import Yandex
import about
import Firefox
import variables as var
import get_messages as mes


def show_about_win():
    about.show_about_info(datetime.now().year, root)


def start_clean_firefox():
    if Firefox.check_mozilla():
        var.thread_stop = False
        var.files_counter = 0
        var.all_files = 0
        var.size = 0

        def check_thread(thread):
            if thread.is_alive():
                btn_1_ch_ver_firefox.configure(state='disabled')
                btn_2_cl_cache_firefox.configure(state='disabled')
                btn_3_ch_ver_yandex.configure(state='disabled')
                btn_4_cl_cache_firefox.configure(state='disabled')
                root.after(100, lambda: check_thread(thread))
            else:
                progressbar.stop()
                label_progress_counter.configure(text=f'100 %', foreground='black')
                label_progress.configure(text=f'Очищено: {var.files_deleted} / {var.cache_start}')
                btn_1_ch_ver_firefox.configure(state='normal')
                btn_2_cl_cache_firefox.configure(state='normal')
                btn_3_ch_ver_yandex.configure(state='normal')
                btn_4_cl_cache_firefox.configure(state='normal')
                var.thread_stop = False

        progressbar.start()
        label_progress.configure(text=f'0/0')
        label_progress_counter.configure(text=f'Идет удаление файлов...', foreground='green')
        thread = threading.Thread(target=Firefox.solo_clean_cache(progressbar, label_progress, label_progress_counter), daemon=False)
        thread.start()
        check_thread(thread)
    else:
        mes.error('Проверка установки браузера', 'Mozilla Firefox не найден на вашем АРМ!')


def start_clean_yandex():
    if Yandex.check_ya_browser():
        var.thread_stop = False
        var.files_counter = 0
        var.all_files = 0
        var.size = 0

        def check_thread(thread):
            if thread.is_alive():
                btn_1_ch_ver_firefox.configure(state='disabled')
                btn_2_cl_cache_firefox.configure(state='disabled')
                btn_3_ch_ver_yandex.configure(state='disabled')
                btn_4_cl_cache_firefox.configure(state='disabled')
                root.after(100, lambda: check_thread(thread))
            else:
                progressbar.stop()
                label_progress_counter.configure(text=f'100 %', foreground='black')
                label_progress.configure(text=f'Очищено: {var.files_deleted} / {var.cache_start}')
                btn_1_ch_ver_firefox.configure(state='normal')
                btn_2_cl_cache_firefox.configure(state='normal')
                btn_3_ch_ver_yandex.configure(state='normal')
                btn_4_cl_cache_firefox.configure(state='normal')
                var.thread_stop = False

        label_progress.configure(text=f'0/0')
        label_progress_counter.configure(text=f'Идет удаление файлов...', foreground='green')
        progressbar.start()
        thread = threading.Thread(target=Yandex.solo_clean_cache(progressbar, label_progress, label_progress_counter), daemon=False)
        thread.start()
        check_thread(thread)
    else:
        mes.error('Проверка установки браузера', 'На вашем АРМ не обнаружен Яндекс.Браузер!')


root = Tk()
root.title('Очистка кэша')
root.geometry('450x370+200+200')
root.resizable(True, False)
root.minsize(450, 370)
root.maxsize(450, 370)
s = ttk.Style()
s.theme_use('alt')
style = TTk.ThemedStyle(root)
style.set_theme("breeze")
appImgB64 = """iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAACXBIWXMAAAsTAAALEwEAmpwYAAACEklEQVR4nO2W30tiQRTH/QPrphX0stXDqhu99NI+eCtpjbyuEtqPhyUodp9iXzbKNCsjuTdNHwoiKjEiLArZDMqKXXBv3+UMJTchvFHaSHfgC4eZM9/5cJgzjMlUj6NJDH4RHCFVEEOohRrFkNrQF3bqBqQNE9Es5BxKIiPf4uWrSBBDj7xHV7IQHAuqbsByg2oDyvf+BqDPqOAz7mD+WoXeMa0Uan8H4wd/dQNSbs0Bp+SCbsCLG9XoYhjvoPjKd9DoYu2wO/zQ6q262F7G8QgwuX1Q0lt9FpIaBgPQ9+4qaC9rkkDkCDObF1g9+Vc1wOhxkZ1BZ1VsEm1XU/Lgz118Gouj2RlBpzfGDLomttAzuYvPPzLon8nC9esMrtkc3MFzSME8vOFLJoppjtYoh3J7v2fYXvIgrw7vGvOmM+is8oe6IuBD6WNnd5hP38Izl0Hv1CZso3G0e2Joc62gdXAZLc4lWAYiMPcvQhDDTBTTHK1RTttQFB1fY2wveZAXeZL3U78Z3YC1kmAA5uqggkpQgbKwzing0S1SLa1MFHMHmPCOI221If3RymK+APfzSDU04trjYaJY2fvND2BCCuCwuxt//H4mijekAD+ASbMFV253CfBqeJjNcQOYMltQ0AAWJAkpczM/gImRb9j50M7ASBTTHDeA8mmRAVHVSAzutMgRYO7lMgDlaleQR5nqYfwHZJC3/vq9cOcAAAAASUVORK5CYII="""
appImgP = tk.PhotoImage(data=appImgB64)
root.iconphoto(False, appImgP)

menu = Menubutton(root, text='Помощь')
options = Menu(menu)
menu.config(menu=options)
options.add_command(label='О программе', command=show_about_win)
menu.pack(anchor='w')


f1 = Frame(root)
f1.pack(fill=X, padx=10, pady=3)

f2 = Frame(root)
f2.pack(fill=X, padx=10, pady=3)

f3 = Frame(root)
f3.pack(fill=X, padx=10, pady=3)

f4 = Frame(root)
f4.pack(fill=X, padx=10, pady=3)

f5 = Frame(root)
f5.pack(fill=X, padx=10, pady=3)

f6 = Frame(root)
f6.pack(fill=X, padx=10, pady=3)

s.configure('my.TButton', font=('Verdana', 11))

label1 = ttk.Label(f1, text='1', style='my.TButton', width=1)
label1.pack(side=LEFT, ipadx=1, ipady=6, pady=5)

btn_1_ch_ver_firefox = ttk.Button(f1, text='Узнать версию "Firefox"', command=Firefox.find_firefox, width=35,
                                  style='my.TButton')
btn_1_ch_ver_firefox.pack(side=LEFT, ipadx=5, ipady=5, pady=5)

label2 = ttk.Label(f2, text='2', style='my.TButton', width=1)
label2.pack(side=LEFT, ipadx=1, ipady=6, pady=5)

btn_2_cl_cache_firefox = ttk.Button(f2, text='Очистка кэша "Firefox"', command=start_clean_firefox, width=35,
                                    style='my.TButton')
btn_2_cl_cache_firefox.pack(side=LEFT, ipadx=5, ipady=5, pady=5)

label3 = ttk.Label(f3, text='3', style='my.TButton', width=1)
label3.pack(side=LEFT, ipadx=1, ipady=6, pady=5)

btn_3_ch_ver_yandex = ttk.Button(f3, text='Узнать версию "Яндекс.Браузера"', command=Yandex.find_ya_browser,
                                 width=35, style='my.TButton')
btn_3_ch_ver_yandex.pack(side=LEFT, ipadx=5, ipady=5, pady=5)

label4 = ttk.Label(f4, text='4', style='my.TButton', width=1)
label4.pack(side=LEFT, ipadx=1, ipady=6, pady=5)

btn_4_cl_cache_firefox = ttk.Button(f4, text='Очистка кэша "Яндекс.Браузера"', width=35, style='my.TButton',
                                    command=start_clean_yandex)
btn_4_cl_cache_firefox.pack(side=LEFT, ipadx=5, ipady=5, pady=5)

progressbar = ttk.Progressbar(f5, orient="horizontal", value=var.progress, mode='indeterminate',
                              maximum=var.max_progress, length=410)
progressbar.pack(side=LEFT, ipadx=5, ipady=5, pady=5)

label_progress = ttk.Label(f6, text='0/0', style='my.TButton')
label_progress.pack(side=LEFT, ipadx=1, ipady=6, pady=5)

label_progress_counter = ttk.Label(f6, text='0 %', style='my.TButton')
label_progress_counter.pack(side=RIGHT, ipadx=1, ipady=6, pady=5, padx=15)

root.mainloop()
