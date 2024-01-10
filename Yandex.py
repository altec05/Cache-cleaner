import os
from pathlib import Path
import pathlib
from tkinter import messagebox
import time
import clean_func as clean
import get_messages as mes
import variables as var
from clean_func import check_path


# Перебираем файлы в полученной папке.
# Убираем начало пути из строки.
# Убираем слэш.
# Убираем точки.
# Сравниваем полученное целое число с ранее максимальным и записываем
def get_ya_version(paths, dir_path):
    if len(paths) > 0:
        max_int = 0
        max_ver = ''
        for path in paths:
            check_path = (str(path).replace(str(dir_path)+'\\', '')).replace('.', '')
            if check_path.isdigit():
                if max_int < int(check_path):
                    max_int = int(check_path)
                    max_ver = (str(path).replace(str(dir_path)+'\\', ''))
        return max_ver
    else:
        return ''


def check_ya_browser():
    paths = list()
    appdata_paths = list()
    if check_path(Path(var.ya_browser_version_path)):
        paths = sorted(Path(var.ya_browser_version_path).iterdir(), key=os.path.getmtime)
    if check_path(Path(var.local_appdata_ya_ver_path)):
        appdata_paths = sorted(Path(var.local_appdata_ya_ver_path).iterdir(), key=os.path.getmtime)
    try:
        version = get_ya_version(appdata_paths, var.local_appdata_ya_ver_path)
        if version == '':
            version = get_ya_version(paths, var.ya_browser_version_path)
            if version == '':
                return False
            else:
                return True
        else:
            return True
    except Exception as e:
        return False


# поиск версии Yandex Browser
def find_ya_browser():
    paths = list()
    appdata_paths = list()
    if check_path(Path(var.ya_browser_version_path)):
        paths = sorted(Path(var.ya_browser_version_path).iterdir(), key=os.path.getmtime)
    if check_path(Path(var.local_appdata_ya_ver_path)):
        appdata_paths = sorted(Path(var.local_appdata_ya_ver_path).iterdir(), key=os.path.getmtime)
    try:
        version = get_ya_version(appdata_paths, var.local_appdata_ya_ver_path)
        if version == '':
            version = get_ya_version(paths, var.ya_browser_version_path)
            if version == '':
                mes.error('Версия Яндекс.Браузера', f'Яндекс.Браузер не найден на вашем АРМ!')
            else:
                mes.info('Версия Яндекс.Браузера', f'Версия установленного Яндекс браузера: {version}')
        else:
            mes.info('Версия Яндекс.Браузера', f'Версия Яндекс браузера: {version}')
    except Exception as e:
        mes.error('Ошибка определения версии браузера', f'Причина: %s' % e)


# закрываем все экземпляры Яндекс Браузера перед очисткой
def kill_yandex():
    if clean.kill_process('browser'):
        time.sleep(0.5)
        return True
    else:
        return False


def clean_vars():
    var.cache_listed = 0
    var.cache_start = 0
    var.cache_end = 0
    var.files_counter = 0
    var.all_files = 0
    var.cache_count = 0
    var.files_deleted = 0


def files_counter():
    cache_counter = 0

    path = var.ya_browser_cache_path
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            cache_path = os.path.join(path, root, dir)
            cache_files = len(os.listdir(cache_path))
            cache_counter += cache_files
            print(var.cache_count)

    return cache_counter


# находим кэш и удаляем
def solo_clean_cache(progressbar, label_progress, label_progress_counter):
    while not var.thread_stop:
        res = messagebox.askquestion('Очистка браузера', 'ВНИМАНИЕ!\n\nОчистка может занять продолжительное время.\n\nНачать очистку сейчас?')
        if res == 'yes':

            # Очищаем глобальные переменные перед запуском
            clean_vars()

            # Подсчитываем изначальное количество файлов
            var.cache_start = files_counter()

            # функция удаления содержимого директории
            cache_deleted = 0
            del_res = 0
            try:
                path = var.ya_browser_cache_path
                for root, dirs, files in os.walk(path):
                    for dir in dirs:
                        cache_path = os.path.join(path, root, dir)
                        cache_files = len(os.listdir(cache_path))
                        var.max_progress = cache_files
                        var.cache_count += cache_files
                        print(var.cache_count)
                        if var.cache_count > 0:
                            del_res = clean.clean_foo(cache_path, cache_files, progressbar, label_progress, label_progress_counter)
                            if del_res == 0:
                                continue
                            else:
                                cache_deleted += del_res
            except Exception as e:
                mes.error(f'Ошибка подготовки к очистке', 'Причина: %s' % e)
                continue

            if var.cache_count > 0:
                # Подсчитываем оставшееся количество файлов
                var.cache_end = files_counter()
                var.files_deleted = var.cache_listed - var.cache_end

                mes.info('Очистка кэша', f'Объектов обнаружено: {var.cache_start}.\nОбъектов очищено:'
                                         f' {var.files_deleted}')
            else:
                mes.warning('Очистка кэша', 'Очистка в данный момент не требуется, т.к. не обнаружено временных файлов')
            var.thread_stop = True
            var.clean_yandex_done = True
        else:
            mes.warning('Отмена очистки', 'Очистка была отменена.')
            var.thread_stop = True
        var.thread_stop = True
