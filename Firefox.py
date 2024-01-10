import os
from tkinter import messagebox

import winapps
import time
import clean_func as clean
import get_messages as mes
import variables as var


def check_mozilla():
    flag = False
    for app in winapps.search_installed('Mozilla Firefox'):
        flag = True
        print(flag)
        return True
    flag = False
    print(flag)
    return False


# поиск версии Mozilla Firefox среди установленных
def find_firefox():
    versions = list()
    names = list()
    for app in winapps.list_installed():
        if 'irefox' in app.name:
            versions.append(app.version)
            names.append(app.name)
    out = ''
    i = 0
    for version in versions:
        out += names[i] + ': ' + version + '\n'

    if versions != '':
        mes.info('Версия браузера Firefox', f'{out}')
    else:
        mes.error('Версия браузера Firefox', f'Mozilla Firefox не найден на вашем АРМ!')


# закрываем все экземпляры firefox перед очисткой
def kill_firefox():
    if clean.kill_process('firefox'):
        time.sleep(0.5)
        return True
    else:
        return False


# Подсчитываем количество файлов в папках Firefox
def files_counter():
    cache_counter = 0
    path = var.firefox_profiles_path
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir == 'cache':
                cache_path = os.path.join(path, root, dir)
                for cache_root, cache_dirs, cache_files in os.walk(cache_path):
                    for cache_dir in cache_dirs:
                        cache_dir_path = os.path.join(cache_path, cache_root, cache_dir)
                        in_cache_files = len(os.listdir(cache_dir_path))
                        cache_counter += in_cache_files
                cache_files = len(os.listdir(cache_path))
                cache_counter += cache_files
            elif dir == 'cache2':
                cache_path = os.path.join(path, root, dir)
                for cache_root, cache_dirs, cache_files in os.walk(cache_path):
                    for cache_dir in cache_dirs:
                        cache_dir_path = os.path.join(cache_path, cache_root, cache_dir)
                        in_cache_files = len(os.listdir(cache_dir_path))
                        cache_counter += in_cache_files
                cache_files = len(os.listdir(cache_path))
                cache_counter += cache_files
            elif dir == 'thumbnails':
                cache_path = os.path.join(path, root, dir)
                cache_files = len(os.listdir(cache_path))
                cache_counter += cache_files
            else:
                continue
    return cache_counter


def clean_vars():
    var.cache_listed = 0
    var.cache_start = 0
    var.cache_end = 0
    var.files_counter = 0
    var.all_files = 0
    var.cache_count = 0
    var.files_deleted = 0


# находим кэш и удаляем
def solo_clean_cache(progressbar, label_progress, label_progress_counter):
        res = messagebox.askquestion('Очистка браузера', 'ВНИМАНИЕ!\n\nОчистка может занять продолжительное время.\nТакже рекомендуется закрыть браузер для полной очистки врмененных файлов.\n\nНачать очистку сейчас?')
        if res == 'yes':
            # Очищаем глобальные переменные перед запуском
            clean_vars()

            # Подсчитываем изначальное количество файлов
            var.cache_start = files_counter()

            # функция удаления содержимого директории
            cache_deleted = 0
            del_res = 0
            try:
                path = var.firefox_profiles_path
                for root, dirs, files in os.walk(path):
                    for dir in dirs:
                        if dir == 'cache':
                            cache_path = os.path.join(path, root, dir)

                            for cache_root, cache_dirs, cache_files in os.walk(cache_path):
                                for cache_dir in cache_dirs:
                                    cache_dir_path = os.path.join(cache_path, cache_root, cache_dir)
                                    in_cache_files = len(os.listdir(cache_dir_path))
                                    print(f'\nПо пути {cache_dir_path} файлов: {in_cache_files}')
                                    var.max_progress = in_cache_files
                                    var.cache_count += in_cache_files
                                    del_res = clean.clean_foo(cache_dir_path, in_cache_files, progressbar, label_progress,
                                                              label_progress_counter)
                                    if del_res == 0:
                                        continue
                                    else:
                                        cache_deleted += del_res
                            cache_files = len(os.listdir(cache_path))
                            del_res = clean.clean_foo(cache_path, cache_files, progressbar, label_progress, label_progress_counter)
                            if del_res == 0:
                                continue
                            else:
                                cache_deleted += del_res
                        elif dir == 'cache2':
                            cache_path = os.path.join(path, root, dir)

                            for cache_root, cache_dirs, cache_files in os.walk(cache_path):
                                for cache_dir in cache_dirs:
                                    cache_dir_path = os.path.join(cache_path, cache_root, cache_dir)
                                    in_cache_files = len(os.listdir(cache_dir_path))
                                    print(f'\nПо пути {cache_dir_path} файлов: {in_cache_files}')
                                    var.max_progress = in_cache_files
                                    var.cache_count += in_cache_files
                                    del_res = clean.clean_foo(cache_dir_path, in_cache_files, progressbar, label_progress,
                                                              label_progress_counter)
                                    if del_res == 0:
                                        continue
                                    else:
                                        cache_deleted += del_res
                            cache_files = len(os.listdir(cache_path))
                            del_res = clean.clean_foo(cache_path, cache_files, progressbar, label_progress, label_progress_counter)
                            if del_res == 0:
                                continue
                            else:
                                cache_deleted += del_res
                        elif dir == 'thumbnails':
                            cache_path = os.path.join(path, root, dir)
                            cache_files = len(os.listdir(cache_path))
                            var.cache_count += cache_files
                            del_res = clean.clean_foo(cache_path, cache_files, progressbar, label_progress, label_progress_counter)
                            if del_res == 0:
                                continue
                            else:
                                cache_deleted += del_res
                        else:
                            continue
            except Exception as e:
                mes.error(f'Ошибка получения файлов для очистки', 'Причина: %s' % e)
                var.thread_stop = True

            if var.cache_count > 0:
                # Подсчитываем оставшееся количество файлов
                var.cache_end = files_counter()
                var.files_deleted = var.cache_listed - var.cache_end

                mes.info('Очистка кэша', f'Объектов обнаружено: {var.cache_start}.\nОбъектов очищено:'
                                         f' {var.files_deleted}')

                var.thread_stop = True
            else:
                mes.warning('Очистка кэша', 'Очистка в данный момент не требуется, т.к. не обнаружено временных файлов')
                var.thread_stop = True
        else:
            mes.warning('Отмена очистки', 'Очистка была отменена.')
            var.thread_stop = True
        var.thread_stop = True
