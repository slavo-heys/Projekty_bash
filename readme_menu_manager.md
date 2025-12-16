# 🎨 Menu Manager - Graficzne menu TUI dla skryptów Bash

## 🇵🇱 Polski

### Opis
**Menu Manager** to nowoczesna aplikacja konsolowa z graficznym interfejsem użytkownika (TUI) napisana w Pythonie z wykorzystaniem biblioteki `textual`. Zapewnia przyjazne wizualne menu do uruchamiania skryptów bash z pełną obsługą klawiatury i myszy.

### ✨ Funkcje
- 🎨 Piękny interfejs tekstowy w stylu Midnight Commander
- 🖱️ Pełna obsługa myszy i klawiatury
- ⌨️ Skróty klawiszowe (1, 2, Q, ESC)
- 🎯 Nawigacja strzałkami + Enter
- 📊 Pole statusu z informacjami
- 🌈 Kolorowe przyciski i ramki
- ⏰ Zegar w nagłówku
- 📱 Responsywny design

### 📋 Wymagania
- **Python**: 3.8 lub nowszy
- **Biblioteka**: textual

### 🔧 Instalacja

1. **Zainstaluj textual:**
   ```bash
   pip install textual
   ```

2. **Nadaj uprawnienia wykonywania:**
   ```bash
   chmod +x menu_manager.py
   ```

### 🚀 Użycie

```bash
./menu_manager.py
```
lub
```bash
python3 menu_manager.py
```

### ⌨️ Skróty klawiszowe

| Klawisz | Akcja |
|---------|-------|
| `1` | Uruchom Copier SCP |
| `2` | Uruchom Updater |
| `↑ ↓` | Nawigacja między przyciskami |
| `Enter` | Wybierz aktywny przycisk |
| `Q` / `ESC` | Wyjście z programu |
| `Klik myszy` | Wybierz przycisk |

### 🎮 Dostępne opcje

#### 📁 Copier SCP
Uruchamia skrypt `copier_scp.sh` do kopiowania plików przez SSH.

#### 🔄 Updater
Uruchamia skrypt `updater.sh` do aktualizacji systemu Linux.

#### 📖 Pomoc
Wyświetla informacje o dostępnych skrótach klawiszowych.

#### ❌ Wyjście
Zamyka aplikację Menu Manager.

### 📸 Interfejs

```
┌──────────────────────────────────────────────────────┐
│ 🐧 Linux Scripts Manager                             │
│ Wybierz narzędzie do uruchomienia                    │
│                                                       │
│ ┌──────────────────────────────────────────────────┐ │
│ │ 📁 Copier SCP - Kopiowanie plików przez SSH      │ │
│ └──────────────────────────────────────────────────┘ │
│                                                       │
│ ┌──────────────────────────────────────────────────┐ │
│ │ 🔄 Updater - Aktualizacja systemu Linux          │ │
│ └──────────────────────────────────────────────────┘ │
│                                                       │
│ ┌──────────────────────────────────────────────────┐ │
│ │ 📖 Pomoc - Wyświetl informacje                   │ │
│ └──────────────────────────────────────────────────┘ │
│                                                       │
│ ┌──────────────────────────────────────────────────┐ │
│ │ ❌ Wyjście                                        │ │
│ └──────────────────────────────────────────────────┘ │
│                                                       │
│ Status: Gotowy                                        │
└──────────────────────────────────────────────────────┘
```

### 🎨 Personalizacja

Plik zawiera sekcję CSS, którą możesz modyfikować:

```python
CSS = """
    # Kolory, rozmiary, marginesy...
    Button {
        width: 100%;
        margin: 1;
    }
"""
```

### 🔧 Rozszerzanie

Dodawanie nowego przycisku:

1. Dodaj przycisk w metodzie `compose()`:
```python
yield Button(
    "🆕 Nowy Skrypt",
    id="new_script",
    variant="primary"
)
```

2. Dodaj obsługę w `on_button_pressed()`:
```python
elif button_id == "new_script":
    self.action_run_new_script()
```

3. Dodaj metodę akcji:
```python
def action_run_new_script(self) -> None:
    script_path = os.path.join(self.script_dir, "new_script.sh")
    if os.path.exists(script_path):
        self.exit()
        subprocess.run(["bash", script_path])
```

### 💡 Wskazówki
- Program automatycznie wychodzi przed uruchomieniem skryptu
- Skrypty muszą być w tym samym katalogu co `menu_manager.py`
- Pole statusu pokazuje komunikaty o błędach
- Zegar w nagłówku pokazuje aktualny czas

### ⚠️ Rozwiązywanie problemów

**Błąd: `ModuleNotFoundError: No module named 'textual'`**
```bash
pip install --user textual
```

**Błąd: `Nie znaleziono skryptu`**
- Upewnij się, że skrypty `.sh` są w tym samym katalogu
- Sprawdź uprawnienia wykonywania skryptów

---

## 🇬🇧 English

### Description
**Menu Manager** is a modern console application with graphical user interface (TUI) written in Python using the `textual` library. It provides a friendly visual menu for launching bash scripts with full keyboard and mouse support.

### ✨ Features
- 🎨 Beautiful text interface in Midnight Commander style
- 🖱️ Full mouse and keyboard support
- ⌨️ Keyboard shortcuts (1, 2, Q, ESC)
- 🎯 Arrow navigation + Enter
- 📊 Status field with information
- 🌈 Colorful buttons and borders
- ⏰ Clock in header
- 📱 Responsive design

### 📋 Requirements
- **Python**: 3.8 or newer
- **Library**: textual

### 🔧 Installation

1. **Install textual:**
   ```bash
   pip install textual
   ```

2. **Set execution permissions:**
   ```bash
   chmod +x menu_manager.py
   ```

### 🚀 Usage

```bash
./menu_manager.py
```
or
```bash
python3 menu_manager.py
```

### ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `1` | Run Copier SCP |
| `2` | Run Updater |
| `↑ ↓` | Navigate between buttons |
| `Enter` | Select active button |
| `Q` / `ESC` | Exit program |
| `Mouse click` | Select button |

### 🎮 Available Options

#### 📁 Copier SCP
Launches `copier_scp.sh` script for copying files via SSH.

#### 🔄 Updater
Launches `updater.sh` script for Linux system updates.

#### 📖 Help
Displays information about available keyboard shortcuts.

#### ❌ Exit
Closes the Menu Manager application.

### 🎨 Customization

File contains CSS section that you can modify:

```python
CSS = """
    # Colors, sizes, margins...
    Button {
        width: 100%;
        margin: 1;
    }
"""
```

### 🔧 Extending

Adding a new button:

1. Add button in `compose()` method:
```python
yield Button(
    "🆕 New Script",
    id="new_script",
    variant="primary"
)
```

2. Add handler in `on_button_pressed()`:
```python
elif button_id == "new_script":
    self.action_run_new_script()
```

3. Add action method:
```python
def action_run_new_script(self) -> None:
    script_path = os.path.join(self.script_dir, "new_script.sh")
    if os.path.exists(script_path):
        self.exit()
        subprocess.run(["bash", script_path])
```

### 💡 Tips
- Program automatically exits before running script
- Scripts must be in the same directory as `menu_manager.py`
- Status field shows error messages
- Header clock shows current time

### ⚠️ Troubleshooting

**Error: `ModuleNotFoundError: No module named 'textual'`**
```bash
pip install --user textual
```

**Error: `Script not found`**
- Make sure `.sh` scripts are in the same directory
- Check script execution permissions

---

## 📄 License
Free to use and modify.

## 👤 Author
black | Version 1.0 | 2025-12-12
