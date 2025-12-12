# 🐧 Projekty Bash - Narzędzia dla Linux

Kolekcja użytecznych skryptów Bash do automatyzacji codziennych zadań w systemie Linux. Te narzędzia oszczędzają czas eliminując potrzebę wielokrotnego wpisywania tych samych poleceń.

## 📦 Programy

### 📁 copier_scp.sh
Interaktywny skrypt do bezpiecznego kopiowania plików ze zdalnych serwerów przez protokół SSH/SCP.

**Funkcje:**
- 🔐 Kopiowanie plików przez SSH z uwierzytelnieniem hasłem
- 💬 Przyjazny interfejs użytkownika
- ✅ Automatyczna weryfikacja narzędzi
- 📊 Informacyjne komunikaty o statusie

📖 [Szczegółowa dokumentacja](readmi_copier_sh.md)

### 🔄 updater.sh
Skrypt do automatyzacji procesu aktualizacji systemu Linux z obsługą różnych menedżerów pakietów.

**Funkcje:**
- 🎯 Menu wyboru typu aktualizacji
- 📦 Obsługa APT i YUM
- 🧹 Automatyczne czyszczenie po aktualizacji
- 🔄 Różne tryby aktualizacji (standard/full)

📖 [Szczegółowa dokumentacja](readme_updater_sh.md)

## 🚀 Szybki start

```bash
# Nadaj uprawnienia wykonywania
chmod +x *.sh

# Uruchom wybrany skrypt
./copier_scp.sh
# lub
./updater.sh
```

## 📋 Wymagania

- System: Linux/Unix
- Shell: Bash
- Uprawnienia: sudo (dla updater.sh)

## 📄 Licencja

Wolne do użytku i modyfikacji.

---

# 🐧 Bash Projects - Linux Tools

Collection of useful Bash scripts to automate daily tasks in Linux systems. These tools save time by eliminating the need to repeatedly type the same commands.

## 📦 Programs

### 📁 copier_scp.sh
Interactive script for securely copying files from remote servers via SSH/SCP protocol.

**Features:**
- 🔐 File copying over SSH with password authentication
- 💬 User-friendly interface
- ✅ Automatic tool verification
- 📊 Informative status messages

📖 [Detailed documentation](readmi_copier_sh.md)

### 🔄 updater.sh
Script for automating Linux system update process with support for different package managers.

**Features:**
- 🎯 Update type selection menu
- 📦 APT and YUM support
- 🧹 Automatic cleanup after updates
- 🔄 Different update modes (standard/full)

📖 [Detailed documentation](readme_updater_sh.md)

## 🚀 Quick Start

```bash
# Grant execution permissions
chmod +x *.sh

# Run selected script
./copier_scp.sh
# or
./updater.sh
```

## 📋 Requirements

- System: Linux/Unix
- Shell: Bash
- Permissions: sudo (for updater.sh)

## 📄 License

Free to use and modify.