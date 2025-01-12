import os
import subprocess
import json

def load_game_profile(profile_path):
    """
    Загружает профиль игры из JSON файла.

    :param profile_path: Путь к JSON файлу профиля.
    :return: Имя пользователя.
    """
    try:
        with open(profile_path, 'r', encoding='utf-8') as profile_file:
            profile = json.load(profile_file)
            return profile.get('username', 'Player')
    except FileNotFoundError:
        print(f"Не вдалося знайти файл профілю: {profile_path}")
        return 'Player'
    except json.JSONDecodeError:
        print(f"Помилка декодування JSON у файлі профілю: {profile_path}")
        return 'Player'

def launch_minecraft(java_path, minecraft_jar, profile_path, memory="2G", extra_flags=None):
    """
    Запускает Minecraft с заданными параметрами.

    :param java_path: Путь к Java-исполняемому файлу.
    :param minecraft_jar: Путь к Minecraft JAR-файлу.
    :param profile_path: Путь к профилю игры (JSON файл).
    :param memory: Максимальный объем памяти (например, "2G").
    :param extra_flags: Дополнительные флаги запуска.
    """
    username = load_game_profile(profile_path)

    if extra_flags is None:
        extra_flags = []

    # Основные флаги запуска Minecraft
    flags = [
        java_path,
        f"-Xmx{memory}",        # Максимальный объем памяти
        f"-Xms{memory}",        # Минимальный объем памяти
        "-XX:+UseG1GC",         # Использование Garbage Collector G1
        "-XX:+UnlockExperimentalVMOptions",  # Разблокировка экспериментальных настроек
        "-XX:MaxGCPauseMillis=50",  # Уменьшение пауз GC
        "-XX:G1NewSizePercent=20",  # Настройки G1GC
        "-XX:G1ReservePercent=20",
        "-XX:InitiatingHeapOccupancyPercent=15",
        "-XX:SoftRefLRUPolicyMSPerMB=50",
        "-XX:SurvivorRatio=8",
        "-XX:+OptimizeStringConcat",
        "-XX:+UseCompressedOops",
        "-jar", minecraft_jar,  # Указываем JAR-файл Minecraft
        "--username", username  # Указываем имя пользователя
    ]

    # Добавляем дополнительные флаги, если они указаны
    flags.extend(extra_flags)

    try:
        # Запускаем Minecraft
        subprocess.run(flags, check=True)
    except FileNotFoundError:
        print("Переконайтеся, що шлях до Java та JAR-файлу Minecraft вказано правильно.")
    except subprocess.CalledProcessError as e:
        print(f"Помилка при запуску Minecraft: {e}")

# Пример использования
if __name__ == "__main__":
    # Замените пути на актуальные для вашей системы
    JAVA_PATH = "C:/Program Files (x86)/Java/jre1.8.0_431/bin/java.exe"  # Путь к Java
    MINECRAFT_JAR = r"%APPDATA%/Roaming/.epohahublauncher/game/versions/1.19.2.jar"  # Путь к Minecraft JAR
    PROFILE_PATH = r"%APPDATA%/Roaming/.epohahublauncher/config.json"  # Путь к профилю игры (JSON файл)
    MEMORY = "10G"  # Память, выделенная под Minecraft

    # Запуск лаунчера
    launch_minecraft(JAVA_PATH, MINECRAFT_JAR, PROFILE_PATH, MEMORY)
