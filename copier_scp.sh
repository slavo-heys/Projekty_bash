#!/usr/bin/env bash

#######################################
# Opis: Kopiowanie pliku z serwera przez SSH
# Autor: black
# Data: 2025-12-12
# Wersja: 1.1
#######################################

# Opcje bezpieczeństwa
set -euo pipefail  # Zatrzymaj przy błędach, nieokreślonych zmiennych i błędach w pipeline

# Sprawdź czy sshpass jest zainstalowany
if ! command -v sshpass &> /dev/null; then
    echo "Błąd: sshpass nie jest zainstalowany!"
    echo "Zainstaluj: sudo apt install sshpass"
    exit 1
fi

# Pobierz adres IP
read -p "Podaj adres IP: " ip_address
echo

# Pobierz nazwę użytkownika
read -p "Podaj nazwę użytkownika: " username
echo

# Pobierz hasło użytkownika
read -sp "Podaj hasło użytkownika: " password
echo

# Pobierz ścieżkę do pliku
read -p "Podaj ścieżkę i nazwę do pliku na serwerze: " file_path
echo

# Pobierz lokalną ścieżkę do pliku
read -p "Podaj lokalną ścieżkę gdzie zapisać plik: " local_path
echo

# Rozpoczynam kopiowanie pliku za pomocą SCP
echo "Kopiowanie pliku w toku..."
if sshpass -p "$password" scp "${username}@${ip_address}:${file_path}" "${local_path}"; then
    echo
    echo "✓ Plik skopiowany pomyślnie do: ${local_path}"
else
    echo
    echo "✗ Błąd podczas kopiowania pliku!"
    exit 1
fi

echo
echo "Koniec skryptu."