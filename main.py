import json
import uuid
import requests
import subprocess
import os
import sys
import zipfile
from tqdm import tqdm

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

GAME_FOLDER = os.path.expandvars(r"%APPDATA%\roaming\.epohahublaunher\game")
DROPBOX_FILES = {
    "mods.zip": "https://www.dropbox.com/scl/fo/mewqtgcfe381xqtfetq7t/AH2cLAfh1WRBUXEPSw-LbVM?rlkey=g0i5rxod3deh648hnvzs8dmuy&st=bagav94e&dl=1",  # Посилання на моди
    "config.zip": "https://www.dropbox.com/scl/fo/csgsulr4xd7b9evph9b2y/AJTxVLm91iMpkkUfdKs4I5g?rlkey=8vjz6rna0oibwxf8tuwvwppxe&st=lpy91tu4&dl=1"  # Посилання на конфігурації
}

def download_file(url, destination):
    """Завантаження файлу за вказаним URL з прогрес-баром."""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))  # Загальний розмір файлу
    block_size = 1024  # Розмір блоку
    t = tqdm(total=total_size, unit='B', unit_scale=True, desc=f"Завантаження {os.path.basename(destination)}")

    with open(destination, 'wb') as file:
        for chunk in response.iter_content(block_size):
            t.update(len(chunk))
            file.write(chunk)
    t.close()

    if t.n != total_size:
        print("Попередження: Завантажено не всі дані!")
    else:
        print(f"Файл успішно завантажено: {destination}")

def extract_zip(file_path, extract_to):
    """Розпаковка ZIP-архіву у вказану папку."""
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Файли розпаковано у: {extract_to}")

def setup_game():
    """Основна функція для завантаження та встановлення модів і конфігурацій."""
    if not os.path.exists(GAME_FOLDER):
        os.makedirs(GAME_FOLDER)
        print(f"Створено папку гри: {GAME_FOLDER}")

    for file_name, url in DROPBOX_FILES.items():
        local_file_path = os.path.join(GAME_FOLDER, file_name)
        print(f"Завантаження файлу: {file_name}")
        download_file(url, local_file_path)

        # Якщо файл ZIP, розпакувати його
        if file_name.endswith(".zip"):
            print(f"Розпаковка архіву: {file_name}")
            extract_zip(local_file_path, GAME_FOLDER)
            os.remove(local_file_path)  # Видалення архіву після розпаковки

if __name__ == "__main__":
    setup_game()


# 8. Запуск гри
#Воно кароче поки не робе не скоро зделаю но в test.py є поки накидки


