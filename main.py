import time
import threading
import keyboard
from utils.screenshot import save_screenshot_from_clipboard
from config import SLEEP_TIME
from winotify import Notification

def show_notification(title, message):
    try:
        toast = Notification(app_id="ScreenshotApp", title=title, msg=message)
        toast.show()
    except Exception as e:
        print(f"[Erro ao mostrar notificação] {e}")

def capture_task():
    try:
        time.sleep(0.15)  # tempo para o clipboard carregar a imagem
        save_screenshot_from_clipboard()
        show_notification("📸 Captura salva", "Screenshot salva com sucesso!")
    except Exception as e:
        print(f"[Erro na captura] {e}")

def main():
    print("🖼️ Monitorando tecla Print Screen... (Ctrl+C para sair)")

    # Atalho para iniciar a captura
    keyboard.add_hotkey('print screen', lambda: threading.Thread(target=capture_task).start())

    try:
        while True:
            time.sleep(1)  # mantém o programa rodando
    except KeyboardInterrupt:
        print("\n👋 Programa encerrado pelo usuário.")
    finally:
        keyboard.unhook_all_hotkeys()

if __name__ == "__main__":
    main()
