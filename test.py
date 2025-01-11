import subprocess
import os

# Шляхи до файлів Minecraft
minecraft_dir = os.path.expandvars(r"%APPDATA%\.epohahublauncher\game")  # Папка Minecraft
version = "1.19.2"  # Ваша версія Forge
java_path = r"C:\Program Files\Java\jdk-17\bin\java.exe"  # Шлях до Java (змініть за необхідності)

libraries_path = os.path.expandvars(r"%APPDATA%\.epohahublauncher\game\libraries")
jar_file = os.path.expandvars(r"%APPDATA%\.epohahublauncher\game\versions\1.19.2\1.19.2.jar")
natives_path = os.path.expandvars(r"%APPDATA%\.epohahublauncher\game\versions\1.19.2\natives")
game_dir = os.path.expandvars(r"%APPDATA%\.epohahublauncher\game")
assets_dir = os.path.expandvars(r"%APPDATA%\.epohahublauncher\game\assets")

# Формируем classpath
classpath = f"{jar_file};{libraries_path}\\*"

# Команда для запуска
command = [
    java_path,
    "-Xmx2G",
    "-Xms1G",
    f"-Djava.library.path={natives_path}",
    "-cp", classpath,
    "net.minecraft.launchwrapper.Launch",
    "--username", "Player",
    "--version", version,
    "--gameDir", game_dir,
    "--assetsDir", assets_dir,
    "--assetIndex", "1.19",
    "--tweakClass", "net.minecraftforge.fml.common.launcher.FMLTweaker"
]

# Запуск
try:
    subprocess.run(command, check=True)
    print("Minecraft успішно запущено!")
except subprocess.CalledProcessError as e:
    print(f"Помилка запуску: {e}")
except Exception as e:
    print(f"Непередбачена помилка: {e}")
