import json
import uuid
import requests
import subprocess
import os
import shutil
import sys
import stat
import errno

# Директория для лаунчера
LAUNCHER_DIR = os.path.expandvars(r"%APPDATA%\.epohahublauncher")
GAME_DIR = os.path.join(LAUNCHER_DIR, "game")
CONFIG_FILE = os.path.join(LAUNCHER_DIR, "config.json")

# Створення директорій
os.makedirs(LAUNCHER_DIR, exist_ok=True)
os.makedirs(GAME_DIR, exist_ok=True)

# 1. Запит ніку та збереження UUID
if not os.path.exists(CONFIG_FILE):
    config = {}
else:
    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)

if 'nickname' not in config:
    nickname = input("Введіть свій нікнейм: ")
    user_uuid = str(uuid.uuid4())
    config['nickname'] = nickname
    config['uuid'] = user_uuid
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)
    print(f"Привіт, {config['nickname']}! Ваш UUID: {config['uuid']}")
else:
    print(f"Привіт, {config['nickname']}! Ваш UUID: {config['uuid']}")

# 2. Завантаження Java 17 якщо її немає

def is_java_17_installed():
    try:
        output = subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT, text=True)
        print(f"Вихідна інформація про версію Java: {output}")
        if "17" in output:
            print("Java 17 вже встановлена.")
            return True
        else:
            print("Java 17 не встановлена.")
            return False
    except FileNotFoundError:
        print("Java не знайдена на комп'ютері.")
        return False
    except subprocess.CalledProcessError as e:
        print(f"Помилка при виконанні команди перевірки версії Java: {e}")
        return False

if not is_java_17_installed():
    print("Запуск скрипта для встановлення Java 17...")
    try:
        os.system("python java17download.py")
    except Exception as e:
        print(f"Помилка при запуску скрипта java17download.py: {e}")
    sys.exit("Java 17 не встановлена. Будь ласка, перезапустіть програму після встановлення Java 17.")

# 3. Заванатження Git

def check_git():
    try:
        subprocess.run(["git", "--version"], check=True)
        print("Git вже встановлено.")
    except subprocess.CalledProcessError:
        print("Git не знайдено. Запуск файлу GitDownload.py для встановлення Git.")
        subprocess.run([sys.executable, "git-download.py"])

if __name__ == "__main__":
    check_git()


# 4. Завантаження Forge 1.19.2

import os
import sys
import requests

def print_progress_bar(iteration, total, length=50):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r|{bar}| {percent}% Complete')
    sys.stdout.flush()

def download_forge():
    forge_url = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.19.2-43.4.0/forge-1.19.2-43.4.0-installer.jar"
    launcher_dir = os.path.expandvars(r"%APPDATA%\.epohahublauncher")
    output_path = os.path.join(launcher_dir, 'Forge-1.19.2.jar')

    if os.path.exists(output_path):
        print("Файл Forge-1.19.2.jar вже існує. Пропускаємо завантаження.")
        return

    response = requests.get(forge_url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte

    with open(output_path, 'wb') as file:
        for data in response.iter_content(block_size):
            file.write(data)
            print_progress_bar(file.tell(), total_size)

    print("\nЗавантаження Forge завершено!")


if __name__ == "__main__":
    download_forge()

# 5. Створення профілю

try:
    subprocess.run(["python", "profile.py"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Помилка при запуску скрипта java17download.py: {e}")

# 6. Установка Forge 1.19.2

launcher_dir = os.path.expandvars(r"%APPDATA%\.epohahublauncher")
jar_path = os.path.join(launcher_dir, 'Forge-1.19.2.jar')

try:
    subprocess.run(["java", "-jar", jar_path], check=True)
    print("Установка Forge-1.19.2.jar прошла успішно.")
except subprocess.CalledProcessError as e:
    print(f"Помилка при запуску Forge-1.19.2.jar: {e}")

# 7. Завантаження модів

# URL репозиторію
repo_url = "https://github.com/kirilo987/mods.git"
# Локальний шлях для клонування репозиторію
local_repo_path = os.path.join(os.getenv('APPDATA'), '.epohahublauncher', 'temp_repo')
# Шлях для вигрузки файлів
destination_path = os.path.join(os.getenv('APPDATA'), '.epohahublauncher', 'game')

def handle_remove_readonly(func, path, exc):
    excvalue = exc[1]
    if func in (os.rmdir, os.remove, os.unlink) and excvalue.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
        func(path)
    else:
        raise

def sync_files():
    print("Видалення старої копії репозиторію...")
    if os.path.exists(local_repo_path):
        shutil.rmtree(local_repo_path, onerror=handle_remove_readonly)

    print("БУДЬ ЛАСКА НЕ ВИМИКАЙТЕ ЦЕ\nКлонування репозиторію з модами...")
    subprocess.run(["git", "clone", repo_url, local_repo_path])

    files = [f for f in os.listdir(local_repo_path) if f != '.git']
    total_files = len(files)

    print("Копіювання файлів до призначеного шляху...")
    for i, item in enumerate(files, 1):
        source = os.path.join(local_repo_path, item)
        destination = os.path.join(destination_path, item)

        if os.path.isdir(source):
            shutil.copytree(source, destination, dirs_exist_ok=True)
        else:
            shutil.copy2(source, destination)

        print_progress_bar(i, total_files)

    print("\nСинхронізація завершена!")

sync_files()

# 8. Запуск гри



