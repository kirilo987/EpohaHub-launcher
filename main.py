import os
import json
import uuid
import requests
import zipfile

# Директория лаунчера
LAUNCHER_DIR = os.path.expandvars(r"%APPDATA%\.epohahublauncher")
CONFIG_FILE = os.path.join(LAUNCHER_DIR, "config.json")
MODS_DIR = os.path.join(LAUNCHER_DIR, "mods")

# Створення папок
os.makedirs(LAUNCHER_DIR, exist_ok=True)
os.makedirs(MODS_DIR, exist_ok=True)

# 1. Запит ніку та збереження UUID
if not os.path.exists(CONFIG_FILE):
    nickname = input("Введіть свій нікнейм: ")
    user_uuid = str(uuid.uuid4())
    config = {"nickname": nickname, "uuid": user_uuid}
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)
else:
    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)
    print(f"Привіт, {config['nickname']}! Ваш UUID: {config['uuid']}")

# 2. Завантаження та встановлення Forge
def install_forge(version="1.19.2"):
    forge_url = f"https://files.minecraftforge.net/maven/net/minecraftforge/forge/{version}/forge-{version}-installer.jar"
    forge_path = os.path.join(LAUNCHER_DIR, "forge-installer.jar")
    print("Завантаження Forge...")
    response = requests.get(forge_url)
    if response.status_code == 200:
        with open(forge_path, "wb") as f:
            f.write(response.content)
        print("Forge завантажено.")
    else:
        print("Помилка завантаження Forge!")

install_forge()

# 3. Інтеграція зі skLauncher (el.by) для скінів
def download_skin(nickname):
    skin_url = f"https://skins.el.by/{nickname}.png"
    skin_path = os.path.join(LAUNCHER_DIR, "skin.png")
    response = requests.get(skin_url)
    if response.status_code == 200:
        with open(skin_path, "wb") as f:
            f.write(response.content)
        print(f"Скін завантажено для {nickname}.")
    else:
        print("Не вдалося завантажити скін.")

download_skin(config["nickname"])

# 4. Синхронізація модів із базою даних
def sync_mods(server_url="http://example.com/api/mods"):
    print("Синхронізація модів...")
    response = requests.get(server_url)
    if response.status_code == 200:
        mods = response.json()
        for mod in mods:
            mod_path = os.path.join(MODS_DIR, mod["filename"])
            if not os.path.exists(mod_path):
                print(f"Завантаження мода: {mod['name']}...")
                mod_data = requests.get(mod["url"])
                with open(mod_path, "wb") as f:
                    f.write(mod_data.content)
        print("Моди синхронізовані.")
    else:
        print("Помилка підключення до сервера модів.")

sync_mods()

