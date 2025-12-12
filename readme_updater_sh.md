# 🔄 Updater - Automatyczna aktualizacja systemu Linux

## 🇵🇱 Polski

### Opis
**Updater** to interaktywny skrypt Bash do automatyzacji procesu aktualizacji systemów Linux. Obsługuje zarówno dystrybucje oparte na Debian/Ubuntu (APT), jak i RedHat/CentOS (YUM), oferując przyjazne menu wyboru z różnymi trybami aktualizacji.

### ✨ Funkcje
- 🎯 Interaktywne menu wyboru typu aktualizacji
- 📦 Obsługa menedżerów pakietów APT i YUM
- 🧹 Automatyczne czyszczenie po aktualizacji
- 🔄 Dwa tryby aktualizacji APT:
  - **Standard** (`apt upgrade`) - bezpieczniejszy, zachowuje stabilność
  - **Full upgrade** (`apt full-upgrade`) - pełna aktualizacja z możliwością usuwania pakietów
- 🛡️ Zaawansowane opcje bezpieczeństwa
- ✅ Automatyczne usuwanie niepotrzebnych pakietów
- 🗑️ Czyszczenie cache po aktualizacji

### 📋 Wymagania
- **System**: Linux (Debian/Ubuntu/RedHat/CentOS)
- **Uprawnienia**: sudo/root
- **Menedżer pakietów**: apt lub yum

### 🔧 Instalacja

```bash
chmod +x updater.sh
```

### 🚀 Użycie

```bash
./updater.sh
```

### 📝 Dostępne opcje

#### Opcja 1: Aktualizacja APT (standardowa)
```bash
apt update          # Aktualizacja listy pakietów
apt upgrade -y      # Aktualizacja pakietów (bezpieczna)
apt autoremove -y   # Usunięcie niepotrzebnych pakietów
apt autoclean       # Czyszczenie cache
```
**Zalecana dla**: codziennych aktualizacji, serwerów produkcyjnych

#### Opcja 2: Aktualizacja APT (pełna)
```bash
apt update              # Aktualizacja listy pakietów
apt full-upgrade -y     # Pełna aktualizacja (może usuwać pakiety)
apt autoremove -y       # Usunięcie niepotrzebnych pakietów
apt autoclean           # Czyszczenie cache
```
**Zalecana dla**: większych aktualizacji, przejść między wersjami

#### Opcja 3: Aktualizacja YUM
```bash
yum update -y       # Aktualizacja wszystkich pakietów
yum autoremove -y   # Usunięcie niepotrzebnych pakietów
yum clean all       # Czyszczenie cache
```
**Zalecana dla**: systemów RedHat/CentOS/Fedora

### 💡 Przykład użycia

```
Wybierz opcję aktualizacji:
---------------------------

1) Aktualizuj system (apt update && apt upgrade && apt autoremove && apt autoclean)
2) Aktualizuj system (apt update && apt full-upgrade && apt autoremove && apt autoclean)
3) Aktualizuj system (yum update -y && yum autoremove -y && yum clean all)

Wybierz 1 lub 2: 1

Aktualizacja systemu za pomocą apt...
[sudo] hasło dla black:
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
...
✓ System zaktualizowany pomyślnie!
```

### ⚙️ Różnice między trybami APT

| Funkcja | `apt upgrade` | `apt full-upgrade` |
|---------|---------------|-------------------|
| Aktualizuje pakiety | ✅ | ✅ |
| Instaluje nowe zależności | ❌ | ✅ |
| Usuwa konflikty | ❌ | ✅ |
| Bezpieczeństwo | Wyższe | Niższe |
| Ryzyko problemów | Niskie | Średnie |

### ⚠️ Uwagi
- Skrypt wymaga uprawnień **sudo**
- Przed aktualizacją upewnij się, że masz backup ważnych danych
- Na serwerach produkcyjnych zaleca się opcję 1 (standardowa)
- Opcja 2 może usunąć niektóre pakiety - używaj ostrożnie
- Aktualizacja może zająć kilka minut

### 🔐 Bezpieczeństwo
- Skrypt zatrzymuje się przy pierwszym błędzie (`set -e`)
- Wykrywa nieokreślone zmienne (`set -u`)
- Sprawdza błędy w pipeline'ach (`set -o pipefail`)

### 📊 Planowanie automatyczne (opcjonalnie)

Aby uruchamiać automatycznie, dodaj do crontab:
```bash
# Codziennie o 3:00 rano (wymaga konfiguracji sudo bez hasła)
0 3 * * * /ścieżka/do/updater.sh <<< "1"
```

---

## 🇬🇧 English

### Description
**Updater** is an interactive Bash script for automating the update process of Linux systems. It supports both Debian/Ubuntu-based distributions (APT) and RedHat/CentOS (YUM), offering a user-friendly selection menu with different update modes.

### ✨ Features
- 🎯 Interactive update type selection menu
- 📦 Support for APT and YUM package managers
- 🧹 Automatic cleanup after updates
- 🔄 Two APT update modes:
  - **Standard** (`apt upgrade`) - safer, maintains stability
  - **Full upgrade** (`apt full-upgrade`) - complete update with package removal capability
- 🛡️ Advanced security options
- ✅ Automatic removal of unnecessary packages
- 🗑️ Cache cleanup after updates

### 📋 Requirements
- **System**: Linux (Debian/Ubuntu/RedHat/CentOS)
- **Permissions**: sudo/root
- **Package Manager**: apt or yum

### 🔧 Installation

```bash
chmod +x updater.sh
```

### 🚀 Usage

```bash
./updater.sh
```

### 📝 Available Options

#### Option 1: APT Update (standard)
```bash
apt update          # Update package lists
apt upgrade -y      # Update packages (safe)
apt autoremove -y   # Remove unnecessary packages
apt autoclean       # Clean cache
```
**Recommended for**: daily updates, production servers

#### Option 2: APT Update (full)
```bash
apt update              # Update package lists
apt full-upgrade -y     # Full update (may remove packages)
apt autoremove -y       # Remove unnecessary packages
apt autoclean           # Clean cache
```
**Recommended for**: major updates, version transitions

#### Option 3: YUM Update
```bash
yum update -y       # Update all packages
yum autoremove -y   # Remove unnecessary packages
yum clean all       # Clean cache
```
**Recommended for**: RedHat/CentOS/Fedora systems

### 💡 Usage Example

```
Select update option:
---------------------------

1) Update system (apt update && apt upgrade && apt autoremove && apt autoclean)
2) Update system (apt update && apt full-upgrade && apt autoremove && apt autoclean)
3) Update system (yum update -y && yum autoremove -y && yum clean all)

Choose 1 or 2: 1

Updating system using apt...
[sudo] password for black:
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
...
✓ System updated successfully!
```

### ⚙️ Differences Between APT Modes

| Feature | `apt upgrade` | `apt full-upgrade` |
|---------|---------------|-------------------|
| Updates packages | ✅ | ✅ |
| Installs new dependencies | ❌ | ✅ |
| Removes conflicts | ❌ | ✅ |
| Security | Higher | Lower |
| Risk of issues | Low | Medium |

### ⚠️ Notes
- Script requires **sudo** permissions
- Backup important data before updating
- For production servers, option 1 (standard) is recommended
- Option 2 may remove some packages - use with caution
- Update may take several minutes

### 🔐 Security
- Script stops at first error (`set -e`)
- Detects undefined variables (`set -u`)
- Checks for errors in pipelines (`set -o pipefail`)

### 📊 Automatic Scheduling (optional)

To run automatically, add to crontab:
```bash
# Daily at 3:00 AM (requires sudo without password configuration)
0 3 * * * /path/to/updater.sh <<< "1"
```

---

## 📄 License
Free to use and modify.

## 👤 Author
black | Version 1.1 | 2025-12-12
