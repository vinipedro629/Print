import time
import keyboard
from utils.screenshot import save_screenshot_from_clipboard
from config import SLEEP_TIME

def main():
    print("🖼️  Monitorando tecla Print Screen... (pressione Ctrl+C para parar)")
    while True:
        try:
            if keyboard.is_pressed('print screen'):
                time.sleep(0.3)  # pequeno delay pra clipboard carregar
                save_screenshot_from_clipboard()
                time.sleep(SLEEP_TIME)
        except KeyboardInterrupt:
            print("\n👋 Programa encerrado pelo usuário.")
            break
        except Exception as e:
            print(f"[Erro] {e}")
            time.sleep(1)

if __name__ == "__main__":
    main()
