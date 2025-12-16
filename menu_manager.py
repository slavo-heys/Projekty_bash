#!/usr/bin/env python3
"""
Menu Manager - Graficzne menu dla skryptów bash
Autor: black
Data: 2025-12-12
Wersja: 1.0
"""

from textual.app import App, ComposeResult
from textual.containers import Container, Vertical, Horizontal
from textual.widgets import Header, Footer, Button, Static, Label
from textual.binding import Binding
import subprocess
import os


class MenuManager(App):
    """Aplikacja TUI do zarządzania skryptami bash."""
    
    CSS = """
    Screen {
        align: center middle;
    }
    
    #menu-container {
        width: 80;
        height: auto;
        border: thick $primary;
        background: $surface;
        padding: 2;
    }
    
    #title {
        width: 100%;
        text-align: center;
        color: $accent;
        text-style: bold;
        margin-bottom: 1;
    }
    
    #description {
        width: 100%;
        text-align: center;
        color: $text-muted;
        margin-bottom: 2;
    }
    
    Button {
        width: 100%;
        margin: 1;
    }
    
    .success {
        background: $success;
    }
    
    .warning {
        background: $warning;
    }
    
    .error {
        background: $error;
    }
    
    #status {
        width: 100%;
        height: 3;
        border: solid $primary;
        margin-top: 1;
        padding: 1;
        color: $text;
    }
    """
    
    BINDINGS = [
        Binding("q", "quit", "Wyjście"),
        Binding("1", "run_copier", "Copier"),
        Binding("2", "run_updater", "Updater"),
        Binding("escape", "quit", "ESC"),
    ]
    
    def __init__(self):
        super().__init__()
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
    
    def compose(self) -> ComposeResult:
        """Tworzenie interfejsu aplikacji."""
        yield Header(show_clock=True)
        
        with Container(id="menu-container"):
            yield Static("🐧 Linux Scripts Manager", id="title")
            yield Static("Wybierz narzędzie do uruchomienia", id="description")
            
            with Vertical():
                yield Button(
                    "📁 Copier SCP - Kopiowanie plików przez SSH",
                    id="copier",
                    variant="success"
                )
                yield Button(
                    "🔄 Updater - Aktualizacja systemu Linux",
                    id="updater",
                    variant="primary"
                )
                yield Button(
                    "📖 Pomoc - Wyświetl informacje",
                    id="help",
                    variant="default"
                )
                yield Button(
                    "❌ Wyjście",
                    id="exit",
                    variant="error"
                )
            
            yield Static("", id="status")
        
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Obsługa kliknięć przycisków."""
        button_id = event.button.id
        
        if button_id == "copier":
            self.action_run_copier()
        elif button_id == "updater":
            self.action_run_updater()
        elif button_id == "help":
            self.action_show_help()
        elif button_id == "exit":
            self.action_quit()
    
    def action_run_copier(self) -> None:
        """Uruchom copier_scp.sh."""
        self.update_status("🚀 Uruchamianie copier_scp.sh...")
        script_path = os.path.join(self.script_dir, "copier_scp.sh")
        
        if os.path.exists(script_path):
            self.exit()
            subprocess.run(["bash", script_path])
        else:
            self.update_status(f"❌ Błąd: Nie znaleziono {script_path}")
    
    def action_run_updater(self) -> None:
        """Uruchom updater.sh."""
        self.update_status("🚀 Uruchamianie updater.sh...")
        script_path = os.path.join(self.script_dir, "updater.sh")
        
        if os.path.exists(script_path):
            self.exit()
            subprocess.run(["bash", script_path])
        else:
            self.update_status(f"❌ Błąd: Nie znaleziono {script_path}")
    
    def action_show_help(self) -> None:
        """Wyświetl pomoc."""
        help_text = """
📖 POMOC
─────────────────────────────────────
Klawisze:
  1 - Uruchom Copier SCP
  2 - Uruchom Updater
  Q/ESC - Wyjście
  
Lub użyj myszki/strzałek + Enter
        """
        self.update_status(help_text.strip())
    
    def update_status(self, message: str) -> None:
        """Aktualizuj pole statusu."""
        status = self.query_one("#status", Static)
        status.update(message)
    
    def action_quit(self) -> None:
        """Wyjście z aplikacji."""
        self.exit()


def main():
    """Punkt wejścia aplikacji."""
    app = MenuManager()
    app.run()


if __name__ == "__main__":
    main()
