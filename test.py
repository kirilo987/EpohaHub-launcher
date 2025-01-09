import subprocess
import os

# Шляхи до файлів Minecraft
minecraft_dir = r"%APPDATA%\.epohahublauncher\game"  # Папка Minecraft
version = "1.19.2"  # Ваша версія Forge
java_path = r"C:\Program Files\Java\jdk-17\bin\java.exe"  # Шлях до Java (змініть за необхідності)

libraries_path = r"C:\Users\Kxysl1k\AppData\Roaming\.epohahublauncher\game\libraries"
jar_file = r"C:\Users\Kxysl1k\AppData\Roaming\.epohahublauncher\game\versions\1.19.2\1.19.2.jar"
natives_path = r"C:\Users\Kxysl1k\AppData\Roaming\.epohahublauncher\game\versions\1.19.2\natives"
game_dir = r"C:\Users\Kxysl1k\AppData\Roaming\.epohahublauncher\game"
assets_dir = r"C:\Users\Kxysl1k\AppData\Roaming\.epohahublauncher\game\assets"

classpath = f"{jar_file};{libraries_path}\\*"

command = [
    r"C:\Program Files\Java\jdk-17\bin\java.exe",
    "-Xmx2G",
    "-Xms1G",
    f"-Djava.library.path={natives_path}",
    "-cp", classpath,
    "net.minecraft.launchwrapper.Launch",
    "--username", "Player",
    "--version", "1.19.2",
    "--gameDir", game_dir,
    "--assetsDir", assets_dir,
    "--assetIndex", "1.19",
    "--tweakClass", "net.minecraftforge.fml.common.launcher.FMLTweaker"
]

subprocess.run(command, check=True)


# Запуск
try:
    subprocess.run(command, check=True)
    print("Minecraft успішно запущено!")
except Exception as e:
    print(f"Помилка запуску: {e}")