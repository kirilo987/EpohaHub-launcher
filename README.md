
# 🛠️ EpohaHub Launcher

**EpohaHub Launcher** is a unique Minecraft launcher designed for the most convenient way to launch the game with Forge 1.19.2 modifications. The launcher automates the installation of necessary components such as Java 17, Forge, and mods, allowing players to enjoy the game without extra hassle.

---

## 📌 Features

- **User-friendly setup process:**
  - Automatic download and installation of Java 17 if it's not already installed.
  - Downloading Forge 1.19.2 and configuring the game.
  - Synchronizing mods from a GitHub repository.

- **Profile management:**
  - Saving the player's unique nickname.
  - Generating a UUID for each user.

- **Ease of use:**
  - No need to manually search for mods or install additional components – the launcher does everything for you.

---

## 🚀 How to Install and Use

### 1. Download and install Python 3.13+
Ensure Python is installed, and its path is added to the environment variables.

### 2. Launch the launcher
Run the `main.py` file via Python:
```bash
py main.py
```

### 3. Wait for all processes to complete:
- Checking Java.
- Downloading Forge and mods.
- Creating a player profile.

### 4. Enjoy the game!
The launcher is ready to use. The game can be launched after all the configurations are done.

---

## 🎵 Musical Inspiration
The launcher was created under the influence of the melody [TRASH CAN SONG](https://www.youtube.com/watch?v=M02WlP-ZwD4)

---

## 🛠️ Technical Details

### Core functionality:
1. **Downloading and checking Java:**
   - If Java 17 is missing, the launcher automatically downloads it via a script.

2. **Mod synchronization:**
   - The launcher clones a mod repository from GitHub and copies the files to the appropriate folder.

3. **Forge installation:**
   - Forge 1.19.2 is downloaded from an official source and installed automatically.

4. **Directory management:**
   - The launcher creates necessary folders and files in `%APPDATA%\.epohahublauncher`.

### Dependencies:
- Python 3.13+
- Java 17
- Git

---

## 📋 TODO
- Implement automatic game launch functionality.
- Add support for different Forge versions.
- Expand player profile capabilities.

---

## 🤝 Contacts
Author: **Kxysl1k**  
GitHub: [kirilo987](https://github.com/kirilo987)

---

Enjoy your game with **EpohaHub Launcher**! 🕹️
