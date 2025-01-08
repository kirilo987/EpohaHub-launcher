import os
import subprocess
import platform
import requests
import shutil

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

def download_java_17():
    system = platform.system().lower()
    java_download_url = ""

    # Визначаємо правильне посилання залежно від ОС
    if "windows" in system:
        java_download_url = "https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.exe"
        file_name = "java17-installer.exe"
    elif "linux" in system:
        java_download_url = "https://download.oracle.com/java/17/latest/jdk-17_linux-x64_bin.tar.gz"
        file_name = "java17-linux.tar.gz"
    elif "darwin" in system:  # macOS
        java_download_url = "https://download.oracle.com/java/17/latest/jdk-17_macos-x64_bin.dmg"
        file_name = "java17-macos.dmg"
    else:
        print("Невідома операційна система.")
        return

    # Завантажуємо файл
    print(f"Завантаження Java 17 з {java_download_url}...")
    response = requests.get(java_download_url, stream=True)
    if response.status_code == 200:
        download_path = os.path.join(os.getcwd(), file_name)
        with open(download_path, "wb") as file:
            shutil.copyfileobj(response.raw, file)
        print(f"Java 17 завантажена: {download_path}")
        return download_path
    else:
        print(f"Не вдалося завантажити Java 17. Статус: {response.status_code}")
        return None

def install_java_17(file_path):
    system = platform.system().lower()

    if "windows" in system:
        print("Запуск інсталятора Java 17...")
        subprocess.run([file_path], shell=True)
    elif "linux" in system:
        print("Розпаковка Java 17...")
        subprocess.run(["tar", "-xvf", file_path, "-C", "/usr/local"], shell=True)
    elif "darwin" in system:  # macOS
        print("Відкриття DMG для встановлення Java 17...")
        subprocess.run(["open", file_path], shell=True)
    else:
        print("Встановлення Java не підтримується на цій ОС.")

# Основна логіка
if not is_java_17_installed():
    installer_path = download_java_17()
    if installer_path:
        install_java_17(installer_path)
