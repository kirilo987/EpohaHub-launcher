import os
import requests
from tqdm import tqdm

# URL для завантаження Forge 1.19.2
FORGE_URL = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.19.2-43.4.0/forge-1.19.2-43.4.0-installer.jar"

# Шлях для завантаження файлу
APPDATA_PATH = os.getenv('APPDATA')
TARGET_FOLDER = os.path.join(APPDATA_PATH, ".epohahublauncher")
TARGET_FILE = os.path.join(TARGET_FOLDER, "Forge-1.19.2.jar")

# Створення папки, якщо вона не існує
os.makedirs(TARGET_FOLDER, exist_ok=True)

def download_file(url, target_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(target_path, 'wb') as file, tqdm(
        desc="Завантаження Forge",
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as progress_bar:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)
            progress_bar.update(len(chunk))

if __name__ == "__main__":
    print("Початок завантаження Forge 1.19.2...")
    try:
        download_file(FORGE_URL, TARGET_FILE)
        print(f"Завантаження успішно завершено! Файл збережено в: {TARGET_FILE}")
    except Exception as e:
        print(f"Під час завантаження сталася помилка: {e}")
