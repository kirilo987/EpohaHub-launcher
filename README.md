# 🛠️ EpohaHub Launcher

**EpohaHub Launcher** – це унікальний Minecraft лаунчер, створений для максимально зручного запуску гри з модифікаціями Forge 1.19.2. Лаунчер автоматизує встановлення необхідних компонентів, таких як Java 17, Forge, і моди, щоб гравці могли насолоджуватися грою без зайвих турбот.

---

## 📌 Особливості

- **Інтуїтивно зрозумілий процес налаштування:**
  - Автоматичне завантаження та встановлення Java 17, якщо її немає.
  - Завантаження Forge 1.19.2 та налаштування гри.
  - Синхронізація модів з GitHub-репозиторію.
  
- **Управління профілями:**
  - Збереження унікального ніка гравця.
  - Генерація UUID для кожного користувача.

- **Простота використання:**
  - Не потрібно вручну шукати моди або встановлювати додаткові компоненти – лаунчер робить усе самостійно.

---

## 🚀 Як встановити та використовувати

### 1. Скачайте та встановіть Python 3.13+
Переконайтеся, що Python встановлений, а шлях до нього додано в змінні середовища.

### 2. Запуск лаунчера
Запустіть файл `main.py` через Python:
```bash
python main.py
```

### 3. Дочекайтеся завершення всіх процесів:
- Перевірка Java.
- Завантаження Forge та модів.
- Створення профілю гравця.

### 4. Насолоджуйтеся грою!
Лаунчер готовий до використання. Гру можна запускати після всіх налаштувань.

---

## 🖼️ Скриншоти

### Головна директорія
![Структура директорій](https://via.placeholder.com/800x400?text=Screenshot+1)

### Завантаження модів
![Завантаження модів](https://via.placeholder.com/800x400?text=Screenshot+2)

---

## 🎵 Музичне натхнення
Лаунчер був створений під впливом мелодії [M02WlP-ZwD4](https://www.youtube.com/watch?v=M02WlP-ZwD4). Ви можете увімкнути цей плейлист для занурення в атмосферу:
<iframe width="560" height="315" src="https://www.youtube.com/embed/M02WlP-ZwD4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

## 🛠️ Технічні деталі

### Основний функціонал:
1. **Завантаження та перевірка Java:**
   - Якщо Java 17 відсутня, лаунчер автоматично завантажує її через скрипт.

2. **Синхронізація модів:**
   - Лаунчер клонує репозиторій модів із GitHub і копіює файли до відповідної папки.

3. **Установка Forge:**
   - Forge 1.19.2 завантажується з офіційного джерела та встановлюється автоматично.

4. **Управління директоріями:**
   - Лаунчер створює необхідні папки та файли у `%APPDATA%\.epohahublauncher`.

### Залежності:
- Python 3.13+
- Java 17
- Git

---

## 📋 TODO
- Реалізувати функціонал автоматичного запуску гри.
- Додати підтримку різних версій Forge.
- Розширити можливості профілю гравця.

---

## 🤝 Контакти
Автор: **Kxysl1k**  
GitHub: [kirilo987](https://github.com/kirilo987)

---

Насолоджуйтеся грою з **EpohaHub Launcher**! 🕹️
