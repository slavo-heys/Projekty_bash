#!/usr/bin/env bash

#######################################
# Opis: Automatyzacja aktualizacji systemu Linux
# Autor: black
# Data: 2025-12-12
# Wersja: 1.1
#######################################

# Opcje bezpieczeństwa
set -euo pipefail  # Zatrzymaj przy błędach, nieokreślonych zmiennych i błędach w pipeline

# Krótkie menu aktualizacji
echo "Wybierz opcję aktualizacji:"
echo "---------------------------"
echo
echo "1) Aktualizuj system (apt update && apt upgrade && apt autoremove && apt autoclean)"
echo "2) Aktualizuj system (apt update && apt full-upgrade && apt autoremove && apt autoclean)"
echo "3) Aktualizuj system (yum update -y && yum autoremove -y && yum clean all)"
echo
read -p "Wybierz 1, 2 lub 3: " choice
echo

case $choice in
    1)
        echo "Aktualizacja systemu za pomocą apt..."
        sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y && sudo apt autoclean
        ;;
    2)
        echo "Aktualizacja systemu za pomocą apt (full-upgrade)..."
        sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y && sudo apt autoclean
        ;;    
    3)
        echo "Aktualizacja systemu za pomocą yum..."
        sudo yum update -y
        ;;
    *)
        echo "Nieprawidłowy wybór! Wybierz 1 lub 2."
        exit 1
        ;;
esac    

echo
echo "✓ Aktualizacja zakończona pomyślnie."
echo "Koniec skryptu."  