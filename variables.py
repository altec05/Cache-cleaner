import os

version = '1.2'
last_update = '16.06.2023'

ya_browser_version_path = r"C:\Program Files (x86)\Yandex\YandexBrowser"
local_appdata_ya_ver_path = os.path.join(os.path.join(os.environ['LOCALAPPDATA']), 'Yandex', 'YandexBrowser', 'Application')
ya_browser_cache_path = os.path.join(os.path.join(os.environ['LOCALAPPDATA']), 'Yandex', 'YandexBrowser', 'User Data', 'Default', 'Cache')

firefox_profiles_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'AppData', 'Local', 'Mozilla', 'Firefox', 'Profiles')

step = 0
progress = 0
max_progress = 100
size = 0
all_files = 0
files_counter = 0

cache_count = 0

thread_stop = False
clean_yandex_done = False

cache_start = 0
cache_end = 0
cache_listed = 0
files_deleted = 0

