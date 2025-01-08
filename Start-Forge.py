import subprocess
import os

def run_forge_installer(forge_jar_path):
    if not os.path.isfile(forge_jar_path):
        print(f"Файл {forge_jar_path} не знайдено.")
        return

    try:
        print(f"Запуск інсталятора Forge з {forge_jar_path}...")
        subprocess.run(["java", "-jar", forge_jar_path], check=True)
        print("Встановлення Forge успішно завершено.")
    except subprocess.CalledProcessError as e:
        print(f"Під час запуску інсталятора Forge сталася помилка: {e}")

# Example usage
forge_jar_path = "forge-1.19.2-43.2.0-installer.jar"
run_forge_installer(forge_jar_path)