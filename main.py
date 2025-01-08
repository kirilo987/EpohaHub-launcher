import json
import uuid
import requests
import subprocess
import os
import shutil

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
        # Перевіряємо версію Java
        output = subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT, text=True)
        if "17" in output:
            print("Java 17 вже встановлена.")
            return True
        else:
            print("Java 17 не встановлена.")
            return False
    except FileNotFoundError:
        print("Java не знайдена на комп'ютері.")
        return False

if not is_java_17_installed():
    print("Запуск іншого скрипта для встановлення Java 17...")
    # Запустіть інший Python-скрипт
    os.system("python java17download.py")
else:
    print("Продовження роботи програми...")

# 3. Завантаження Forge 1.19.2

# Шлях до папки та файлу Forge
APPDATA_PATH = os.getenv('APPDATA')
TARGET_FOLDER = os.path.join(APPDATA_PATH, ".epohahublauncher")
TARGET_FILE = os.path.join(TARGET_FOLDER, "Forge-1.19.2.jar")

# Шлях до скрипта, який потрібно запустити, якщо файл відсутній
SECONDARY_SCRIPT = "forge-download.py"

def main():
    if os.path.exists(TARGET_FILE):
        print(f"Forge файл знайдено: {TARGET_FILE}")
    else:
        print(f"Forge файл не знайдено. Запуск іншого скрипта: {SECONDARY_SCRIPT}")
        try:
            subprocess.run(["python", SECONDARY_SCRIPT], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Помилка при запуску скрипта {SECONDARY_SCRIPT}: {e}")

if __name__ == "__main__":
    main()

