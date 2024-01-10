import os
import shutil
import psutil
import get_messages as mes
import subprocess as sp
import variables as var
from pathlib import Path


def check_path(path):
    print(Path(path))
    if Path(path).exists():
        return True
    else:
        return False


# закрываем все экземпляры браузера перед очисткой
def kill_process(proc_name):
    error = False
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if proc_name in proc.info['name']:
                proc.kill()
                error = False
        except:
            error = True
    if error:
        return False
    else:
        return True


# функция очистки файлов в директории
def clean_foo(cache_path, cache_files, progressbar, label_progress, label_progress_counter):
    deleted_files_counter = 0
    print(cache_path, cache_files, type(cache_files))
    if cache_files > 0:
        var.cache_listed += cache_files
        for filename in os.listdir(cache_path):
            file_path = os.path.join(cache_path, filename)
            if os.path.islink(file_path) or os.path.isfile(file_path):
                try:
                    shutil.rmtree(cache_path, ignore_errors=True)
                    deleted_files_counter += 1
                    var.files_counter += 1
                    var.size += var.step
                    label_progress.configure(text=f'Очищено: {var.files_counter} / {var.cache_count}')
                    print(f'var.cache_count = {var.cache_count}')
                except Exception as e:
                    var.size += var.step
                    print(f'var.cache_count = {var.cache_count}')
                    label_progress.configure(text=f'Очищено: {var.files_counter} / {var.cache_count}')
                    continue
            elif os.path.isdir(file_path):
                try:
                    shutil.rmtree(file_path, ignore_errors=True)
                    deleted_files_counter += 1
                    var.files_counter += 1
                    var.size += var.step
                    label_progress.configure(text=f'Очищено: {var.files_counter} / {var.cache_count}')
                    print(f'var.cache_count = {var.cache_count}')
                except Exception as e:
                    var.size += var.step
                    print(f'var.cache_count = {var.cache_count}')
                    label_progress.configure(text=f'Очищено: {var.files_counter} / {var.cache_count}')
                    continue
        return deleted_files_counter
    else:
        return 0
