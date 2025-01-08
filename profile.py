import os
import json

# Шлях до папки та файлу Forge
APPDATA_PATH = os.getenv('APPDATA')
LAUNCHER_FOLDER = os.path.join(APPDATA_PATH, ".epohahublauncher", "game")
LAUNCHER_PROFILES = os.path.join(LAUNCHER_FOLDER, "launcher_profiles.json")

def create_launcher_profiles():
    """Створює базовий файл launcher_profiles.json у папці .epohahublauncher/game"""
    if not os.path.exists(LAUNCHER_FOLDER):
        os.makedirs(LAUNCHER_FOLDER)

    profiles_data = {
        "profiles": {},
        "clientToken": "00000000-0000-0000-0000-000000000000",
        "selectedProfile": "",
        "authenticationDatabase": {},
        "analyticsToken": "",
        "analyticsFailcount": 0,
        "launcherVersion": {
            "name": "custom",
            "format": 21,
            "profilesFormat": 1
        }
    }

    with open(LAUNCHER_PROFILES, "w") as file:
        json.dump(profiles_data, file, indent=4)

    print(f"Файл launcher_profiles.json створено за адресою: {LAUNCHER_PROFILES}")

def main():
    if not os.path.exists(LAUNCHER_PROFILES):
        print("Файл launcher_profiles.json не знайдено. Створюємо...")
        create_launcher_profiles()
    else:
        print(f"Файл launcher_profiles.json вже існує за адресою: {LAUNCHER_PROFILES}")

if __name__ == "__main__":
    main()