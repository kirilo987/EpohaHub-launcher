import subprocess
import os
import sys
import time


def print_progress_bar(iteration, total, length=50):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r|{bar}| {percent}% Complete')
    sys.stdout.flush()


def download_with_progress(url, output_path):
    response = subprocess.run(["curl", "-L", url, "-o", output_path], capture_output=True, text=True)

    # Емуляція процесу завантаження для відображення прогресу
    total_size = 100  # Допустімо загальний розмір файлу 100 одиниць для демонстрації
    for i in range(total_size):
        time.sleep(0.1)  # Емуляція часу завантаження
        print_progress_bar(i + 1, total_size)


def install_git():
    print("Встановлення Git...")
    if os.name == 'nt':
        git_installer_url = "https://github.com/git-for-windows/git/releases/download/v2.34.1.windows.1/Git-2.34.1-64-bit.exe"
        installer_path = os.path.join(os.getenv('APPDATA'), 'Git-Installer.exe')

        # Завантаження Git Installer з прогресом
        download_with_progress(git_installer_url, installer_path)

        # Запуск Git Installer
        subprocess.run([installer_path, "/VERYSILENT", "/NORESTART"])
        print("\nGit встановлено успішно.")
    else:
        print("Автоматичне встановлення Git підтримується лише для Windows.")


if __name__ == "__main__":
    install_git()
