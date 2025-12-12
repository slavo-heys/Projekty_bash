# 📁 Copier SCP - Kopiowanie plików przez SSH

## 🇵🇱 Polski

### Opis
**Copier SCP** to interaktywny skrypt Bash do bezpiecznego kopiowania plików ze zdalnych serwerów przez protokół SSH/SCP. Skrypt automatyzuje proces autoryzacji i transferu plików, oferując przyjazny interfejs użytkownika z weryfikacją błędów.

### ✨ Funkcje
- 🔐 Bezpieczne kopiowanie plików przez SSH z użyciem hasła
- 💬 Interaktywny interfejs - skrypt pyta o wszystkie potrzebne dane
- ✅ Automatyczna weryfikacja czy `sshpass` jest zainstalowany
- 🛡️ Zaawansowane opcje bezpieczeństwa (`set -euo pipefail`)
- 📊 Przyjazne komunikaty o sukcesie/błędzie z ikonami
- 🚫 Zatrzymanie przy pierwszym błędzie

### 📋 Wymagania
- **System**: Linux/Unix z bash
- **Narzędzia**: 
  - `sshpass` - do autoryzacji SSH z hasłem
  - `scp` - do kopiowania plików (zwykle preinstalowane)

### 🔧 Instalacja

1. **Zainstaluj sshpass:**
   ```bash
   sudo apt install sshpass  # Debian/Ubuntu
   # lub
   sudo yum install sshpass  # RedHat/CentOS
   ```

2. **Nadaj uprawnienia wykonywania:**
   ```bash
   chmod +x copier_scp.sh
   ```

### 🚀 Użycie

```bash
./copier_scp.sh
```

Skrypt zapyta o:
1. **Adres IP** serwera zdalnego
2. **Nazwę użytkownika** na serwerze
3. **Hasło** (ukryte podczas wpisywania)
4. **Ścieżkę do pliku** na serwerze zdalnym
5. **Lokalną ścieżkę** gdzie zapisać plik

### 📝 Przykład użycia

```
Podaj adres IP: 192.168.0.140
Podaj nazwę użytkownika: black
Podaj hasło użytkownika: ********
Podaj ścieżkę i nazwę do pliku na serwerze: /home/user/dokument.txt
Podaj lokalną ścieżkę gdzie zapisać plik: /tmp/dokument.txt

Kopiowanie pliku w toku...
✓ Plik skopiowany pomyślnie do: /tmp/dokument.txt
```

### ⚠️ Uwagi bezpieczeństwa
- Hasło jest przechowywane tymczasowo w pamięci - używaj ostrożnie
- Dla lepszego bezpieczeństwa rozważ użycie kluczy SSH zamiast haseł
- Nie uruchamiaj skryptu na niezaufanych systemach

### 🔑 Alternatywa: Klucze SSH (zalecane)
Zamiast używać haseł, można skonfigurować klucze SSH:
```bash
ssh-keygen -t rsa
ssh-copy-id user@adres_ip
```

---

## 🇬🇧 English

### Description
**Copier SCP** is an interactive Bash script for securely copying files from remote servers via SSH/SCP protocol. The script automates the authentication and file transfer process, offering a user-friendly interface with error verification.

### ✨ Features
- 🔐 Secure file copying over SSH with password authentication
- 💬 Interactive interface - script prompts for all required information
- ✅ Automatic verification if `sshpass` is installed
- 🛡️ Advanced security options (`set -euo pipefail`)
- 📊 Friendly success/error messages with icons
- 🚫 Stops at first error

### 📋 Requirements
- **System**: Linux/Unix with bash
- **Tools**: 
  - `sshpass` - for SSH password authentication
  - `scp` - for file copying (usually pre-installed)

### 🔧 Installation

1. **Install sshpass:**
   ```bash
   sudo apt install sshpass  # Debian/Ubuntu
   # or
   sudo yum install sshpass  # RedHat/CentOS
   ```

2. **Set execution permissions:**
   ```bash
   chmod +x copier_scp.sh
   ```

### 🚀 Usage

```bash
./copier_scp.sh
```

The script will ask for:
1. **IP address** of the remote server
2. **Username** on the server
3. **Password** (hidden during input)
4. **File path** on the remote server
5. **Local path** where to save the file

### 📝 Usage Example

```
Enter IP address: 192.168.0.140
Enter username: black
Enter user password: ********
Enter file path on server: /home/user/document.txt
Enter local path to save file: /tmp/document.txt

Copying file in progress...
✓ File successfully copied to: /tmp/document.txt
```

### ⚠️ Security Notes
- Password is temporarily stored in memory - use with caution
- For better security, consider using SSH keys instead of passwords
- Do not run the script on untrusted systems

### 🔑 Alternative: SSH Keys (recommended)
Instead of using passwords, you can configure SSH keys:
```bash
ssh-keygen -t rsa
ssh-copy-id user@ip_address
```

---

## 📄 License
Free to use and modify.

## 👤 Author
black | Version 1.1 | 2025-12-12
